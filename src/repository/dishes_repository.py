from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool

from src.entities.dishes import Dishes


class DishesRepository(ABC):
    @abstractmethod
    def get_all_dishes(self) -> list[Dishes] | None:
        pass


class DishesRepositoryImpl(DishesRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_dishes(self) -> list[Dishes] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.dishes
                        """
                    )
                    dishes = cursor.fetchall()
                    if not dishes:
                        return None
                    return [Dishes(*row) for row in dishes]
        except Exception as e:
            raise ValueError(f"Error retrieving dishes from the database: {e}")
        finally:
            self.conn_pool.putconn(conn)
