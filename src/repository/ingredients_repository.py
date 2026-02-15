from uuid import uuid4
from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError, errorcodes

from src.entities.ingredients import Ingredients


class IngredientsRepository(ABC):
    @abstractmethod
    def get_all_ingredients(self) -> list[Ingredients] | None:
        pass

    @abstractmethod
    def create_ingredient(self) -> list[Ingredients] | None:
        pass

    @abstractmethod
    def get_ingredient(self, ingredient_uuid: str) -> list[Ingredients] | None:
        pass

    @abstractmethod
    def update_ingredient(self, ingredient: Ingredients) -> Ingredients | None:
        pass

    @abstractmethod
    def delete_ingredient(self, ingredient_uuid: str) -> None:
        pass


class IngredientsRepositoryImpl(IngredientsRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_ingredients(self) -> list[Ingredients] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.ingredients
                        """
                    )
                    ingredients = cursor.fetchall()
                    if not ingredients:
                        return None
                    return [Ingredients(*row) for row in ingredients]

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def get_ingredient(self, ingredient_uuid: str) -> list[Ingredients] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:

                    sql = "SELECT * FROM taco.ingredients WHERE uuid = %s"
                    cursor.execute(sql, (ingredient_uuid,))

                    ingredient = cursor.fetchone()

                    if not ingredient:
                        return None

                    return Ingredients(*ingredient)

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def create_ingredient(self, ingredient: Ingredients) -> Ingredients:
        try:
            ingredient.uuid = uuid4()

            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO taco.ingredients (uuid, name) VALUES (%s, %s) RETURNING *"

                    cursor.execute(sql, (str(ingredient.uuid), ingredient.name))

                    inserted = cursor.fetchone()
                    conn.commit()

                    if not inserted:
                        return None

                    return Ingredients(*inserted)

        except DatabaseError as e:
            if getattr(e, 'pgcode', None) == errorcodes.UNIQUE_VIOLATION:
                raise RuntimeError(f"A ingredient with name '{ingredient.name}' already exists.") from e
            raise RuntimeError(f'A database error was found while creating the new ingredient: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while creating the new ingredient: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def update_ingredient(self, ingredient: Ingredients) -> Ingredients | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE taco.ingredients SET name=%s WHERE uuid=%s RETURNING *"

                    cursor.execute(sql, (ingredient.name, ingredient.uuid))

                    updated = cursor.fetchone()
                    conn.commit()

                    if not updated:
                        raise ValueError(f"A ingredient with uuid '{str(ingredient.uuid)}' was not found.")

                    return Ingredients(*updated)

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the ingredient: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the ingredient: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_ingredient(self, ingredient_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.ingredients WHERE uuid = %s"

                    cursor.execute(sql, (ingredient_uuid, ))

                    if cursor.rowcount == 0:
                        raise ValueError(f"A ingredient with uuid '{ingredient_uuid}' was not found.")

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the ingredient: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the ingredient: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)
