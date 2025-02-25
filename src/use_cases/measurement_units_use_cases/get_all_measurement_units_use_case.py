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
        all_measurement_units = {"measurement_units": []}
        for measurement_unit in measurement_units:
            all_measurement_units["measurement_units"].append(
                {
                    "dish_uuid": measurement_unit.uuid,
                    "dish_name": measurement_unit.name
                }
            )

        return all_measurement_units
