# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject
from psycopg2 import pool

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
        except Exception as e:
            raise ValueError(f"Error retrieving measurement units from the database: {e}")
        finally:
            self.conn_pool.putconn(conn)
