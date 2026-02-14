from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError

from src.entities.ingredients import Ingredients


class IngredientsRepository(ABC):
    @abstractmethod
    def get_all_ingredients(self) -> list[Ingredients] | None:
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
