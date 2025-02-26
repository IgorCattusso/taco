# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject
from psycopg2 import pool, DatabaseError

# Project-specific Modules
from src.entities.measurement_units import MeasurementUnits


class MeasurementUnitsRepository(ABC):
    @abstractmethod
    def get_all_measurement_units(self) -> list[MeasurementUnits] | None:
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
