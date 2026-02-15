from abc import ABC, abstractmethod

from injector import inject

from src.repository.nutritional_values_repository import NutritionalValuesRepository
from src.dto.nutritional_value import NutritionalValueDTO


class GetNutritionalValueUseCase(ABC):
    @abstractmethod
    def execute(self, nutritional_value_uuid: str) -> NutritionalValueDTO:
        pass


class GetNutritionalValueUseCaseImpl(GetNutritionalValueUseCase):
    @inject
    def __init__(self, nutritional_values_repository: NutritionalValuesRepository) -> None:
        self.nutritional_values_repository = nutritional_values_repository

    def execute(self, nutritional_value_uuid: str) -> NutritionalValueDTO:
        nutritional_value = self.nutritional_values_repository.get_nutritional_value(nutritional_value_uuid)

        if not nutritional_value:
            raise ValueError("No nutritional value with the supplied UUID was found in the database.")

        nutritional_value_dto = NutritionalValueDTO(
            uuid=nutritional_value.uuid,
            ingredient_uuid=nutritional_value.ingredient_uuid,
            measurement_unit_uuid=nutritional_value.measurement_unit_uuid,
            calories=nutritional_value.calories,
            fats=nutritional_value.fats,
            carbohydrates=nutritional_value.carbohydrates,
            proteins=nutritional_value.proteins,
            sodium=nutritional_value.sodium,
            fiber=nutritional_value.fiber,
        )

        return nutritional_value_dto
