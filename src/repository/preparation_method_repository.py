from uuid import uuid4
from abc import ABC, abstractmethod
from typing import Optional

from injector import inject
from psycopg2 import pool, DatabaseError, errorcodes

from src.entities.preparation_method import PreparationMethod


class PreparationMethodsRepository(ABC):
    @abstractmethod
    def get_all_preparation_methods(self) -> list[PreparationMethod] | None:
        pass

    @abstractmethod
    def get_preparation_method(self, preparation_method_uuid: str) -> PreparationMethod | None:
        pass

    @abstractmethod
    def get_dish_preparation_method(self, dish_uuid: str) -> PreparationMethod | None:
        pass

    @abstractmethod
    def create_preparation_method(self, preparation_method: PreparationMethod) -> PreparationMethod:
        pass

    @abstractmethod
    def update_preparation_method(self, preparation_method: PreparationMethod) -> PreparationMethod | None:
        pass

    @abstractmethod
    def delete_preparation_method(self, preparation_method_uuid: str) -> PreparationMethod | None:
        pass


class PreparationMethodsRepositoryImpl(PreparationMethodsRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_preparation_methods(self) -> list[PreparationMethod] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT uuid, dish_uuid, preparation_method FROM taco.preparation_method
                        """
                    )
                    preparation_methods = cursor.fetchall()
                    if not preparation_methods:
                        return None
                    return [PreparationMethod(*row) for row in preparation_methods]
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e
        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def get_preparation_method(self, preparation_method_uuid: str) -> PreparationMethod | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT uuid, dish_uuid, preparation_method FROM taco.preparation_method WHERE uuid = %s"
                    cursor.execute(sql, (preparation_method_uuid,))

                    preparation_method = cursor.fetchone()

                    if not preparation_method:
                        return None

                    return PreparationMethod(*preparation_method)

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

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

    def create_preparation_method(self, preparation_method: PreparationMethod) -> PreparationMethod:
        try:
            preparation_method.uuid = uuid4()

            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO taco.preparation_method (uuid, dish_uuid, preparation_method) VALUES (%s, %s, %s) RETURNING *"

                    cursor.execute(sql, (str(preparation_method.uuid), preparation_method.dish_uuid, preparation_method.preparation_method))

                    inserted = cursor.fetchone()
                    conn.commit()

                    if not inserted:
                        return None

                    return PreparationMethod(*inserted)

        except DatabaseError as e:
            if getattr(e, 'pgcode', None) == errorcodes.UNIQUE_VIOLATION:
                raise RuntimeError(f"A preparation method for this dish already exists.") from e
            raise RuntimeError(f'A database error was found while creating the new preparation method: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while creating the new preparation method: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def update_preparation_method(self, preparation_method: PreparationMethod) -> PreparationMethod | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE taco.preparation_method SET dish_uuid=%s, preparation_method=%s WHERE uuid=%s RETURNING *"

                    cursor.execute(sql, (preparation_method.dish_uuid, preparation_method.preparation_method, preparation_method.uuid))

                    updated = cursor.fetchone()
                    conn.commit()

                    if not updated:
                        raise ValueError(f"A preparation method with uuid '{str(preparation_method.uuid)}' was not found.")

                    return PreparationMethod(*updated)

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the preparation method: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the preparation method: {e}') from e

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
