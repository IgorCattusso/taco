from abc import ABC, abstractmethod

from injector import inject

from src.repository.ingredients_repository import IngredientsRepository
from src.repository.nutritional_values_repository import NutritionalValuesRepository


class DeleteIngredientUseCase(ABC):
    @abstractmethod
    def execute(self, ingredient_uuid: str) -> dict:
        pass


class DeleteIngredientUseCaseImpl(DeleteIngredientUseCase):
    @inject
    def __init__(self,
                 ingredients_repository: IngredientsRepository,
                 nutritional_values_repository: NutritionalValuesRepository,
            ) -> None:
        self.ingredients_repository = ingredients_repository
        self.nutritional_values_repository = nutritional_values_repository

    def execute(self, ingredient_uuid: str) -> dict:
        self.nutritional_values_repository.delete_nutritional_values_by_ingredient_uuid(ingredient_uuid)
        self.ingredients_repository.delete_ingredient(ingredient_uuid)

        return "Ingredient deleted successfully."
