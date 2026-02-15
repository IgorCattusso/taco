from uuid import uuid4
from abc import ABC, abstractmethod

from injector import inject
from psycopg2 import pool, DatabaseError, errorcodes

from src.entities.measurement_units import MeasurementUnits


class MeasurementUnitsRepository(ABC):
    @abstractmethod
    def get_all_measurement_units(self) -> list[MeasurementUnits] | None:
        pass

    @abstractmethod
    def get_measurement_unit(self, measurement_unit_uuid: str) -> MeasurementUnits | None:
        pass

    @abstractmethod
    def create_measurement_unit(self, measurement_unit: MeasurementUnits) -> MeasurementUnits:
        pass

    @abstractmethod
    def update_measurement_unit(self, measurement_unit: MeasurementUnits) -> MeasurementUnits | None:
        pass

    @abstractmethod
    def delete_measurement_unit(self, measurement_unit_uuid: str) -> None:
        pass


class MeasurementUnitsRepositoryImpl(MeasurementUnitsRepository):
    @inject
    def __init__(self, conn_pool: pool.SimpleConnectionPool):
        self.conn_pool = conn_pool

    def get_all_measurement_units(self) -> list[MeasurementUnits] | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM taco.measurement_units
                        """
                    )
                    measurement_units = cursor.fetchall()
                    if not measurement_units:
                        return None
                    return [MeasurementUnits(*row) for row in measurement_units]
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e
        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def get_measurement_unit(self, measurement_unit_uuid: str) -> MeasurementUnits | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM taco.measurement_units WHERE uuid = %s"
                    cursor.execute(sql, (measurement_unit_uuid,))

                    measurement_unit = cursor.fetchone()

                    if not measurement_unit:
                        return None

                    return MeasurementUnits(*measurement_unit)

        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while retrieving data: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while retrieving data: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def create_measurement_unit(self, measurement_unit: MeasurementUnits) -> MeasurementUnits:
        try:
            measurement_unit.uuid = uuid4()

            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO taco.measurement_units (uuid, name, abbreviation) VALUES (%s, %s, %s) RETURNING *"

                    cursor.execute(sql, (str(measurement_unit.uuid), measurement_unit.name, measurement_unit.abbreviation))

                    inserted = cursor.fetchone()
                    conn.commit()

                    if not inserted:
                        return None

                    return MeasurementUnits(*inserted)

        except DatabaseError as e:
            if getattr(e, 'pgcode', None) == errorcodes.UNIQUE_VIOLATION:
                raise RuntimeError(f"A measurement unit with name '{measurement_unit.name}' already exists.") from e
            raise RuntimeError(f'A database error was found while creating the new measurement unit: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while creating the new measurement unit: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def update_measurement_unit(self, measurement_unit: MeasurementUnits) -> MeasurementUnits | None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE taco.measurement_units SET name=%s, abbreviation=%s WHERE uuid=%s RETURNING *"

                    cursor.execute(sql, (measurement_unit.name, measurement_unit.abbreviation, measurement_unit.uuid))

                    updated = cursor.fetchone()
                    conn.commit()

                    if not updated:
                        raise ValueError(f"A measurement unit with uuid '{str(measurement_unit.uuid)}' was not found.")

                    return MeasurementUnits(*updated)

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while updating the measurement unit: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while updating the measurement unit: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)

    def delete_measurement_unit(self, measurement_unit_uuid: str) -> None:
        try:
            with self.conn_pool.getconn() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM taco.measurement_units WHERE uuid = %s"

                    cursor.execute(sql, (measurement_unit_uuid,))

                    if cursor.rowcount == 0:
                        raise ValueError(f"A measurement unit with uuid '{measurement_unit_uuid}' was not found.")

                    conn.commit()

        except ValueError as e:
            raise e
        except DatabaseError as e:
            raise RuntimeError(f'A database error was found while deleting the measurement unit: {e}') from e
        except Exception as e:
            raise RuntimeError(f'An unexpected error was found while deleting the measurement unit: {e}') from e

        finally:
            if conn:
                self.conn_pool.putconn(conn)
