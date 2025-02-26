# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject
from psycopg2 import pool, DatabaseError

# Project-specific Modules
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
                        return None
                    return [NutritionalValues(*row) for row in nutritional_values]
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e
        finally:
            if conn:
                self.conn_pool.putconn(conn)
