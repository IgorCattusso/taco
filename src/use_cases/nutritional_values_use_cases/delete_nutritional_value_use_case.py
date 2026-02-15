from abc import ABC, abstractmethod

from injector import inject

from src.repository.nutritional_values_repository import NutritionalValuesRepository


class DeleteNutritionalValueUseCase(ABC):
    @abstractmethod
    def execute(self, nutritional_value_uuid: str) -> dict:
        pass


class DeleteNutritionalValueUseCaseImpl(DeleteNutritionalValueUseCase):
    @inject
    def __init__(self, nutritional_values_repository: NutritionalValuesRepository) -> None:
        self.nutritional_values_repository = nutritional_values_repository

    def execute(self, nutritional_value_uuid: str) -> dict:
        self.nutritional_values_repository.delete_nutritional_value(nutritional_value_uuid)

        return "Nutritional value deleted successfully."
