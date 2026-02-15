from uuid import uuid4
from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError, errorcodes

from src.entities.nutritional_values import NutritionalValues


class NutritionalValuesRepository(ABC):
    @abstractmethod
    def get_all_nutritional_values(self) -> list[NutritionalValues] | None:
        pass

    @abstractmethod
    def get_nutritional_value(self, nutritional_value_uuid: str) -> NutritionalValues | None:
        pass

    @abstractmethod
    def create_nutritional_value(self, nutritional_value: NutritionalValues) -> NutritionalValues:
        pass

    @abstractmethod
    def update_nutritional_value(self, nutritional_value: NutritionalValues) -> NutritionalValues | None:
        pass

    @abstractmethod
    def delete_nutritional_value(self, nutritional_value_uuid: str) -> None:
        pass

    @abstractmethod
    def delete_nutritional_values_by_ingredient_uuid(self, ingredient_uuid: str) -> None:
        pass


class NutritionalValuesRepositoryImpl(NutritionalValuesRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_nutritional_values(self) -> list[NutritionalValues] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.nutritional_values
                        """
                    )

                    nutritional_values = cursor.fetchall()
                    if not nutritional_values:
                        return None

                    return [NutritionalValues(*row) for row in nutritional_values]

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def get_nutritional_value(self, nutritional_value_uuid: str) -> NutritionalValues | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM taco.nutritional_values WHERE uuid = %s"
                    cursor.execute(sql, (nutritional_value_uuid,))

                    nutritional_value = cursor.fetchone()

                    if not nutritional_value:
                        return None

                    return NutritionalValues(*nutritional_value)

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def create_nutritional_value(self, nutritional_value: NutritionalValues) -> NutritionalValues:
        try:
            nutritional_value.uuid = uuid4()

            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO taco.nutritional_values (uuid, ingredient_uuid, measurement_unit_uuid, calories, fats, carbohydrates, proteins, sodium, fiber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"

                    cursor.execute(sql, (str(nutritional_value.uuid), nutritional_value.ingredient_uuid, nutritional_value.measurement_unit_uuid, nutritional_value.calories, nutritional_value.fats, nutritional_value.carbohydrates, nutritional_value.proteins, nutritional_value.sodium, nutritional_value.fiber))

                    inserted = cursor.fetchone()
                    conn.commit()

                    if not inserted:
                        return None

                    return NutritionalValues(*inserted)

        except DatabaseError as e:
            if getattr(e, 'pgcode', None) == errorcodes.UNIQUE_VIOLATION:
                raise RuntimeError(f"A nutritional value for this ingredient already exists.") from e
            raise RuntimeError(f'A database error was found while creating the new nutritional value: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while creating the new nutritional value: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def update_nutritional_value(self, nutritional_value: NutritionalValues) -> NutritionalValues | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE taco.nutritional_values SET ingredient_uuid=%s, measurement_unit_uuid=%s, calories=%s, fats=%s, carbohydrates=%s, proteins=%s, sodium=%s, fiber=%s WHERE uuid=%s RETURNING *"

                    cursor.execute(sql, (nutritional_value.ingredient_uuid, nutritional_value.measurement_unit_uuid, nutritional_value.calories, nutritional_value.fats, nutritional_value.carbohydrates, nutritional_value.proteins, nutritional_value.sodium, nutritional_value.fiber, nutritional_value.uuid))

                    updated = cursor.fetchone()
                    conn.commit()

                    if not updated:
                        raise ValueError(f"A nutritional value with uuid '{str(nutritional_value.uuid)}' was not found.")

                    return NutritionalValues(*updated)

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the nutritional value: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the nutritional value: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_nutritional_value(self, nutritional_value_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.nutritional_values WHERE uuid = %s"

                    cursor.execute(sql, (nutritional_value_uuid,))

                    if cursor.rowcount == 0:
                        raise ValueError(f"A nutritional value with uuid '{nutritional_value_uuid}' was not found.")

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while deleting the nutritional value: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while deleting the nutritional value: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_nutritional_values_by_ingredient_uuid(self, ingredient_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.nutritional_values WHERE ingredient_uuid = %s"

                    cursor.execute(sql, (ingredient_uuid, ))

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while deleting the recipe: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while deleting the recipe: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)
