from abc import ABC, abstractmethod

from injector import inject

from src.repository.nutritional_values_repository import NutritionalValuesRepository
from src.entities.nutritional_values import NutritionalValues
from src.dto.nutritional_value import NutritionalValueDTO


class CreateNutritionalValueUseCase(ABC):
    @abstractmethod
    def execute(self, nutritional_value: NutritionalValueDTO) -> dict:
        pass


class CreateNutritionalValueUseCaseImpl(CreateNutritionalValueUseCase):
    @inject
    def __init__(self, nutritional_values_repository: NutritionalValuesRepository) -> None:
        self.nutritional_values_repository = nutritional_values_repository

    def execute(self, nutritional_value: NutritionalValueDTO) -> dict:
        nutritional_value_to_create = NutritionalValues(
            ingredient_uuid=nutritional_value.ingredient_uuid,
            measurement_unit_uuid=nutritional_value.measurement_unit_uuid,
            calories=nutritional_value.calories,
            fats=nutritional_value.fats,
            carbohydrates=nutritional_value.carbohydrates,
            proteins=nutritional_value.proteins,
            sodium=nutritional_value.sodium,
            fiber=nutritional_value.fiber,
        )

        inserted_nutritional_value = self.nutritional_values_repository.create_nutritional_value(nutritional_value_to_create)

        return inserted_nutritional_value.__dict__
