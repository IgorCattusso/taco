from uuid import uuid4
from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError, errorcodes

from src.entities.dishes import Dishes


class DishesRepository(ABC):
    @abstractmethod
    def get_all_dishes(self) -> list[Dishes] | None:
        pass

    @abstractmethod
    def get_dish(self, dish_uuid: str) -> Dishes | None:
        pass

    @abstractmethod
    def create_dish(self, dish: Dishes) -> Dishes:
        pass

    @abstractmethod
    def update_dish(self, dish: Dishes) -> Dishes | None:
        pass

    @abstractmethod
    def delete_dish(self, dish_uuid: str) -> None:
        pass


class DishesRepositoryImpl(DishesRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_dishes(self) -> list[Dishes] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM taco.dishes"

                    cursor.execute(sql)

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

    def get_dish(self, dish_uuid: str) -> list[Dishes] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:

                    sql = "SELECT * FROM taco.dishes WHERE uuid = %s"
                    cursor.execute(sql, (dish_uuid,))

                    dish = cursor.fetchone()

                    if not dish:
                        return None

                    return Dishes(*dish)

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def create_dish(self, dish: Dishes) -> Dishes:
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

    def update_dish(self, dish: Dishes) -> Dishes | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE taco.dishes SET name=%s WHERE uuid=%s RETURNING *"

                    cursor.execute(sql, (dish.name, dish.uuid))

                    updated = cursor.fetchone()
                    conn.commit()

                    if not updated:
                        raise ValueError(f"A dish with uuid '{str(dish.uuid)}' was not found.")

                    return Dishes(*updated)

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the dish: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the dish: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_dish(self, dish_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.dishes WHERE uuid = %s"

                    cursor.execute(sql, (dish_uuid, ))

                    if cursor.rowcount == 0:
                        raise ValueError(f"A dish with uuid '{dish_uuid}' was not found.")

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the dish: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the dish: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)
