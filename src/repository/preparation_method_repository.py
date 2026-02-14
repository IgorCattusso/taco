from abc import ABC, abstractmethod
from typing import Optional

from injector import inject
from psycopg2 import pool, DatabaseError

from src.entities.preparation_method import PreparationMethod


class PreparationMethodsRepository(ABC):
    @abstractmethod
    def get_dish_preparation_method(self, dish_uuid: str) -> PreparationMethod | None:
        pass

    @abstractmethod
    def delete_preparation_method(self, preparation_method_uuid: str) -> PreparationMethod | None:
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

    def delete_preparation_method(self, preparation_method_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.preparation_method WHERE uuid = %s"

                    cursor.execute(sql, (preparation_method_uuid, ))

                    if cursor.rowcount == 0:
                        raise ValueError(f"The preparation method with uuid '{preparation_method_uuid}' was not found.")

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while deleting the preparation method: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while deleting the preparation method: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)
