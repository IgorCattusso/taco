from abc import ABC, abstractmethod

from injector import inject

from src.repository.nutritional_values_repository import NutritionalValuesRepository
from src.entities.nutritional_values import NutritionalValues
from src.dto.nutritional_value import NutritionalValueDTO


class UpdateNutritionalValueUseCase(ABC):
    @abstractmethod
    def execute(self, nutritional_value_uuid: str, nutritional_value: NutritionalValueDTO) -> dict:
        pass


class UpdateNutritionalValueUseCaseImpl(UpdateNutritionalValueUseCase):
    @inject
    def __init__(self, nutritional_values_repository: NutritionalValuesRepository) -> None:
        self.nutritional_values_repository = nutritional_values_repository

    def execute(self, nutritional_value_uuid: str, nutritional_value: NutritionalValueDTO) -> dict:
        nutritional_value_to_update = NutritionalValues(
            uuid=nutritional_value_uuid,
            ingredient_uuid=nutritional_value.ingredient_uuid,
            measurement_unit_uuid=nutritional_value.measurement_unit_uuid,
            calories=nutritional_value.calories,
            fats=nutritional_value.fats,
            carbohydrates=nutritional_value.carbohydrates,
            proteins=nutritional_value.proteins,
            sodium=nutritional_value.sodium,
            fiber=nutritional_value.fiber,
        )

        updated_nutritional_value = \
            self.nutritional_values_repository.update_nutritional_value(nutritional_value_to_update)

        nutritional_value_dto = NutritionalValueDTO(
            uuid=updated_nutritional_value.uuid,
            ingredient_uuid=updated_nutritional_value.ingredient_uuid,
            measurement_unit_uuid=updated_nutritional_value.measurement_unit_uuid,
            calories=updated_nutritional_value.calories,
            fats=updated_nutritional_value.fats,
            carbohydrates=updated_nutritional_value.carbohydrates,
            proteins=updated_nutritional_value.proteins,
            sodium=updated_nutritional_value.sodium,
            fiber=updated_nutritional_value.fiber,
        )

        return nutritional_value_dto.__dict__
