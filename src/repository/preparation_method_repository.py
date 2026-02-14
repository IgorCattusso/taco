from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError

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
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving the preparation method: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving the preparation method: {e}') from e
        finally:
            if conn:
                self.conn_pool.putconn(conn)
