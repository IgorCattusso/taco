# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject
from psycopg2 import pool

# Project-specific Modules
from src.entities.preparation_method import PreparationMethod


class PreparationMethodRepository(ABC):
    @abstractmethod
    def get_all_preparation_method(self) -> list[PreparationMethod] | None:
        pass


class PreparationMethodRepositoryImpl(PreparationMethodRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_preparation_method(self) -> list[PreparationMethod] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.preparation_method
                        """
                    )
                    preparation_method = cursor.fetchall()
                    if not preparation_method:
                        return None
                    return [PreparationMethod(*row) for row in preparation_method]
        except Exception as e:
            raise ValueError(f"Error retrieving preparation method from the database: {e}")
        finally:
            self.conn_pool.putconn(conn)
