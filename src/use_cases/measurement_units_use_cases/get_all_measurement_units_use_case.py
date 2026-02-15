from abc import ABC, abstractmethod

from injector import inject

from src.repository.measurement_units_repository import MeasurementUnitsRepository
from src.dto.measurement_unit import MeasurementUnitDTO


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

        measurement_units_dto = [
            MeasurementUnitDTO(
                uuid=measurement_unit.uuid,
                name=measurement_unit.name,
                abbreviation=measurement_unit.abbreviation,
            ) for measurement_unit in measurement_units
        ]

        return measurement_units_dto
