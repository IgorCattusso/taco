from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool

from src.entities.recipes import Recipes


class RecipesRepository(ABC):
    @abstractmethod
    def get_all_recipes(self) -> list[Recipes] | None:
        pass


class RecipesRepositoryImpl(RecipesRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_recipes(self) -> list[Recipes] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.recipes
                        """
                    )
                    recipes = cursor.fetchall()
                    if not recipes:
                        return None
                    return [Recipes(*row) for row in recipes]
        except Exception as e:
            raise ValueError(f"Error retrieving recipes from the database: {e}")
        finally:
            self.conn_pool.putconn(conn)
