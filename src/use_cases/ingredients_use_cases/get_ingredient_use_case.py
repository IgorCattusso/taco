from abc import ABC, abstractmethod

from injector import inject

from src.repository.ingredients_repository import IngredientsRepository
from src.dto.ingredient import IngredientDTO


class GetIngredientUseCase(ABC):
    @abstractmethod
    def execute(self, ingredient_uuid: str) -> IngredientDTO:
        pass


class GetIngredientUseCaseImpl(GetIngredientUseCase):
    @inject
    def __init__(self, ingredients_repository: IngredientsRepository) -> None:
        self.ingredients_repository = ingredients_repository

    def execute(self, ingredient_uuid: str) -> IngredientDTO:
        ingredient = self.ingredients_repository.get_ingredient(ingredient_uuid)

        if not ingredient:
            raise ValueError("No ingredient with the supplied UUID was found in the database.")

        ingredient_dto = IngredientDTO(uuid=ingredient.uuid, name=ingredient.name)

        return ingredient_dto
