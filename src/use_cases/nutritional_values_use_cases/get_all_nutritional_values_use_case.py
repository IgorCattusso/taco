from abc import ABC, abstractmethod

from injector import inject

from src.repository.nutritional_values_repository import NutritionalValuesRepository
from src.dto.nutritional_value import NutritionalValueDTO


class GetAllNutritionalValuesUseCase(ABC):
    @abstractmethod
    def execute(self) -> list[NutritionalValueDTO]:
        pass


class GetAllNutritionalValuesUseCaseImpl(GetAllNutritionalValuesUseCase):
    @inject
    def __init__(self, nutritional_values_repository: NutritionalValuesRepository) -> None:
        self.nutritional_values_repository = nutritional_values_repository

    def execute(self) -> list[NutritionalValueDTO]:
        nutritional_values = self.nutritional_values_repository.get_all_nutritional_values()

        if not nutritional_values:
            raise ValueError("No nutritional values were found in the database.")

        nutritional_values_dto = [
            NutritionalValueDTO(
                uuid=nutritional_value.uuid,
                ingredient_uuid=nutritional_value.ingredient_uuid,
                measurement_unit_uuid=nutritional_value.measurement_unit_uuid,
                calories=nutritional_value.calories,
                fats=nutritional_value.fats,
                carbohydrates=nutritional_value.carbohydrates,
                proteins=nutritional_value.proteins,
                sodium=nutritional_value.sodium,
                fiber=nutritional_value.fiber,
            ) for nutritional_value in nutritional_values
        ]

        return nutritional_values_dto
