from abc import ABC, abstractmethod

from injector import inject

from src.repository.measurement_units_repository import MeasurementUnitsRepository
from src.dto.measurement_unit import MeasurementUnitDTO


class GetMeasurementUnitUseCase(ABC):
    @abstractmethod
    def execute(self, measurement_unit_uuid: str) -> MeasurementUnitDTO:
        pass


class GetMeasurementUnitUseCaseImpl(GetMeasurementUnitUseCase):
    @inject
    def __init__(self, measurement_units_repository: MeasurementUnitsRepository) -> None:
        self.measurement_units_repository = measurement_units_repository

    def execute(self, measurement_unit_uuid: str) -> MeasurementUnitDTO:
        measurement_unit = self.measurement_units_repository.get_measurement_unit(measurement_unit_uuid)

        if not measurement_unit:
            raise ValueError("No measurement unit with the supplied UUID was found in the database.")

        measurement_unit_dto = MeasurementUnitDTO(
            uuid=measurement_unit.uuid,
            name=measurement_unit.name,
            abbreviation=measurement_unit.abbreviation
        )

        return measurement_unit_dto
