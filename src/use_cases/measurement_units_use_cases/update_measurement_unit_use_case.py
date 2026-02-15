from abc import ABC, abstractmethod

from injector import inject

from src.repository.measurement_units_repository import MeasurementUnitsRepository
from src.entities.measurement_units import MeasurementUnits
from src.dto.measurement_unit import MeasurementUnitDTO


class UpdateMeasurementUnitUseCase(ABC):
    @abstractmethod
    def execute(self, measurement_unit_uuid: str, measurement_unit: MeasurementUnitDTO) -> dict:
        pass


class UpdateMeasurementUnitUseCaseImpl(UpdateMeasurementUnitUseCase):
    @inject
    def __init__(self, measurement_units_repository: MeasurementUnitsRepository) -> None:
        self.measurement_units_repository = measurement_units_repository

    def execute(self, measurement_unit_uuid: str, measurement_unit: MeasurementUnitDTO) -> dict:
        measurement_unit_to_update = MeasurementUnits(
            uuid=measurement_unit_uuid,
            name=measurement_unit.name,
            abbreviation=measurement_unit.abbreviation,
        )

        updated_measurement_unit = self.measurement_units_repository.update_measurement_unit(measurement_unit_to_update)

        measurement_unit_dto = MeasurementUnitDTO(
            uuid=updated_measurement_unit.uuid,
            name=updated_measurement_unit.name,
            abbreviation=updated_measurement_unit.abbreviation,
        )

        return measurement_unit_dto.__dict__
