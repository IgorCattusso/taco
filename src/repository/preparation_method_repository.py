# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject
from psycopg2 import pool

# Project-specific Modules
from src.entities.preparation_method import PreparationMethod


class PreparationMethodsRepository(ABC):
    @abstractmethod
    def get_dish_preparation_method(self, dish_uuid: str) -> PreparationMethod | None:
        pass


class PreparationMethodsRepositoryImpl(PreparationMethodsRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_dish_preparation_method(self, dish_uuid: str) -> PreparationMethod | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT uuid, dish_uuid, preparation_method FROM taco.preparation_method
                        where dish_uuid = %s
                        """,
                        (dish_uuid, )
                    )
                    preparation_method = cursor.fetchone()
                    if not preparation_method:
                        return None
                    return PreparationMethod(*preparation_method)
        except Exception as e:
            raise ValueError(f"Error retrieving preparation method from the database: {e}")
        finally:
            self.conn_pool.putconn(conn)
