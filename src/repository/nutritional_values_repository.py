from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError

from src.entities.nutritional_values import NutritionalValues


class NutritionalValuesRepository(ABC):
    @abstractmethod
    def get_all_nutritional_values(self) -> list[NutritionalValues] | None:
        pass


class NutritionalValuesRepositoryImpl(NutritionalValuesRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_nutritional_values(self) -> list[NutritionalValues] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.nutritional_values
                        """
                    )

                    nutritional_values = cursor.fetchall()
                    if not nutritional_values:
                        raise ValueError("No nutritional values found.")

                    return [NutritionalValues(*row) for row in nutritional_values]

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_nutritional_values_by_ingredient_uuid(self, ingredient_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.nutritional_values WHERE ingredient_uuid = %s"

                    cursor.execute(sql, (ingredient_uuid, ))

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
