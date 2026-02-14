from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError

from src.entities.recipes import Recipe, RecipeIngredients


class RecipesRepository(ABC):
    @abstractmethod
    def get_all_recipes(self) -> list[Recipe] | None:
        pass

    def get_recipe(self, recipe_uuid: str) -> Recipe | None:
        pass

    def get_recipe_by_dish_uuid(self, dish_uuid: str) -> list[RecipeIngredients] | None:
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
