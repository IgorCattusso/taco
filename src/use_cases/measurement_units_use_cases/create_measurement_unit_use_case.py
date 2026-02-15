from abc import ABC, abstractmethod

from injector import inject

from src.repository.measurement_units_repository import MeasurementUnitsRepository
from src.entities.measurement_units import MeasurementUnits
from src.dto.measurement_unit import MeasurementUnitDTO


class CreateMeasurementUnitUseCase(ABC):
    @abstractmethod
    def execute(self, measurement_unit: MeasurementUnitDTO) -> dict:
        pass


class CreateMeasurementUnitUseCaseImpl(CreateMeasurementUnitUseCase):
    @inject
    def __init__(self, measurement_units_repository: MeasurementUnitsRepository) -> None:
        self.measurement_units_repository = measurement_units_repository

    def execute(self, measurement_unit: MeasurementUnitDTO) -> dict:
        measurement_unit_to_create = MeasurementUnits(
            name=measurement_unit.name,
            abbreviation=measurement_unit.abbreviation,
        )

        inserted_measurement_unit = \
            self.measurement_units_repository.create_measurement_unit(measurement_unit_to_create)

        return inserted_measurement_unit.__dict__
