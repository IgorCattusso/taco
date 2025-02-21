from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool

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
        except Exception as e:
            raise ValueError(f"Error retrieving nutritional values from the database: {e}")
        finally:
            self.conn_pool.putconn(conn)
