from uuid import uuid4
from abc import ABC, abstractmethod
from typing import Optional

from injector import inject
from psycopg2 import pool, DatabaseError, errorcodes

from src.entities.dishes import Dishes
from src.dto.dish import Dish


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
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e
        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def create_dish(self, dish: Dish) -> Optional[Dishes] | None:
        try:
            dish.uuid = uuid4()

            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO taco.dishes (uuid, name) VALUES (%s, %s) RETURNING *"

                    cursor.execute(sql, (str(dish.uuid), dish.name))

                    inserted = cursor.fetchone()
                    conn.commit()

                    if not inserted:
                        return None

                    return Dishes(*inserted)

        except DatabaseError as e:
            if getattr(e, 'pgcode', None) == errorcodes.UNIQUE_VIOLATION:
                raise RuntimeError(f"A dish with name '{dish.name}' already exists.") from e

            raise RuntimeError(f'A database error was found while creating the new dish: {e}') from e

        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while creating the new dish: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)
