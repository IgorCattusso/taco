from abc import ABC, abstractmethod

from injector import inject

from src.repository.measurement_units_repository import MeasurementUnitsRepository


class DeleteMeasurementUnitUseCase(ABC):
    @abstractmethod
    def execute(self, measurement_unit_uuid: str) -> dict:
        pass


class DeleteMeasurementUnitUseCaseImpl(DeleteMeasurementUnitUseCase):
    @inject
    def __init__(self, measurement_units_repository: MeasurementUnitsRepository) -> None:
        self.measurement_units_repository = measurement_units_repository

    def execute(self, measurement_unit_uuid: str) -> dict:
        self.measurement_units_repository.delete_measurement_unit(measurement_unit_uuid)

        return "Measurement unit deleted successfully."
