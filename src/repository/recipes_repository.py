from uuid import uuid4
from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError, errorcodes

from src.entities.recipes import Recipe, RecipeIngredients


class RecipesRepository(ABC):
    @abstractmethod
    def get_all_recipes(self) -> list[Recipe] | None:
        pass

    @abstractmethod
    def get_recipe(self, recipe_uuid: str) -> Recipe | None:
        pass

    @abstractmethod
    def get_recipe_by_dish_uuid(self, dish_uuid: str) -> list[RecipeIngredients] | None:
        pass

    @abstractmethod
    def create_recipe(self, recipe: Recipe) -> Recipe:
        pass

    @abstractmethod
    def update_recipe(self, recipe: Recipe) -> Recipe | None:
        pass

    @abstractmethod
    def delete_recipe(self, recipe_uuid: str) -> None:
        pass

    @abstractmethod
    def delete_recipe_by_dish_uuid(self, dish_uuid: str) -> None:
        pass


class RecipesRepositoryImpl(RecipesRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_recipes(self) -> list[Recipe] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.recipes
                        """
                    )
                    recipes = cursor.fetchall()
                    if not recipes:
                        return None
                    return [Recipe(*row) for row in recipes]
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e
        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def get_recipe(self, recipe_uuid: str) -> Recipe | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM taco.recipes WHERE uuid = %s"
                    cursor.execute(sql, (recipe_uuid,))

                    recipe = cursor.fetchone()

                    if not recipe:
                        return None

                    return Recipe(*recipe)

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def get_recipe_by_dish_uuid(self, dish_uuid: str) -> list[RecipeIngredients] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        select
                            r.uuid,
                            r.dish_uuid,
                            nv.ingredient_uuid,
                            nv.measurement_unit_uuid,
                            d.name as "dish_name",
                            i.name as "ingredient_name",
                            mu.abbreviation as "measurement_unit",
                            r.quantity
                        from
                            recipes r
                        join dishes d on
                            d.uuid = r.dish_uuid
                        join nutritional_values nv on
                            nv.uuid = r.nutritional_value_uuid
                        join ingredients i on
                            i.uuid = nv.ingredient_uuid
                        join measurement_units mu on
                            mu.uuid = nv.measurement_unit_uuid
                        where dish_uuid = %s
                        """,
                        (dish_uuid, )
                    )

                    recipe = cursor.fetchall()

                    if recipe:
                        return [RecipeIngredients(*row) for row in recipe]

                    return None

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def create_recipe(self, recipe: Recipe) -> Recipe:
        try:
            recipe.uuid = uuid4()

            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = \
                        """
                        INSERT INTO taco.recipes 
                        (uuid, dish_uuid, nutritional_value_uuid, quantity) 
                        VALUES (%s, %s, %s, %s) RETURNING *
                        """

                    cursor.execute(
                        sql,
                        (
                            str(recipe.uuid),
                            recipe.dish_uuid,
                            recipe.nutritional_value__uuid,
                            recipe.quantity
                        )
                    )

                    inserted = cursor.fetchone()
                    conn.commit()

                    if not inserted:
                        return None

                    return Recipe(*inserted)

        except DatabaseError as e:
            if getattr(e, 'pgcode', None) == errorcodes.UNIQUE_VIOLATION:
                raise RuntimeError('A recipe with these parameters already exists.') from e
            raise RuntimeError(f'A database error was found while creating the new recipe: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while creating the new recipe: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def update_recipe(self, recipe: Recipe) -> Recipe | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = \
                        """
                        UPDATE taco.recipes
                        SET dish_uuid=%s, nutritional_value_uuid=%s, quantity=%s
                        WHERE uuid=%s RETURNING *
                        """

                    cursor.execute(
                        sql,
                        (
                            recipe.dish_uuid,
                            recipe.nutritional_value__uuid,
                            recipe.quantity,
                            recipe.uuid
                        )
                    )

                    updated = cursor.fetchone()
                    conn.commit()

                    if not updated:
                        raise ValueError(f"A recipe with uuid '{str(recipe.uuid)}' was not found.")

                    return Recipe(*updated)

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the recipe: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the recipe: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_recipe(self, recipe_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.recipes WHERE uuid = %s"

                    cursor.execute(sql, (recipe_uuid,))

                    if cursor.rowcount == 0:
                        raise ValueError(f"A recipe with uuid '{recipe_uuid}' was not found.")

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while deleting the recipe: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while deleting the recipe: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_recipe_by_dish_uuid(self, dish_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.recipes WHERE dish_uuid = %s"

                    cursor.execute(sql, (dish_uuid, ))

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while deleting the recipe: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while deleting the recipe: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)
