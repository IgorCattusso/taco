# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject

# Project-specific Modules
from src.repository.measurement_units_repository import MeasurementUnitsRepository


class GetAllMeasurementUnitsUseCase(ABC):
    @abstractmethod
    def execute(self) -> dict:
        pass


class GetAllMeasurementUnitsUseCaseImpl(GetAllMeasurementUnitsUseCase):
    @inject
    def __init__(self, measurement_units_repository: MeasurementUnitsRepository) -> None:
        self.measurement_units_repository = measurement_units_repository

    def execute(self) -> dict:
        measurement_units = self.measurement_units_repository.get_all_measurement_units()

        if not measurement_units:
            raise ValueError("No measurement units were found in the database.")

        return {
            "measurement_units": [{
                "measurement_unit_uuid": measurement_unit.uuid, 
                "measurement_unit_name": measurement_unit.name,
                "measurement_unit_abbreviation": measurement_unit.abbreviation,
            } for measurement_unit in measurement_units]
        }
