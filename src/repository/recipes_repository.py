from abc import ABC, abstractmethod
from injector import inject
from psycopg2 import pool

from src.entities.recipe import Recipe


class RecipesRepository(ABC):
    @abstractmethod
    def get_recipe_of_dish(self, recipe_id: int):
        pass

class RecipesRepositoryImpl(RecipesRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_recipe_of_dish(self, recipe_id: int):
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM ...
                        """,
                        (recipe_id,)
                    )
                    board_structure = cursor.fetchall()
                    if not board_structure:
                        return None
                    return [Recipe(*row) for row in board_structure]
        except Exception as e:
            raise ValueError(f"Error retrieving board structure from the database: {e}") from e
        finally:
            self.conn_pool.putconn(conn)
