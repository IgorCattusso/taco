from abc import ABC, abstractmethod

from injector import inject

from src.repository.ingredients_repository import IngredientsRepository
from src.entities.ingredients import Ingredients
from src.dto.ingredient import IngredientDTO


class CreateIngredientUseCase(ABC):
    @abstractmethod
    def execute(self, ingredient: dict) -> dict:
        pass


class CreateIngredientUseCaseImpl(CreateIngredientUseCase):
    @inject
    def __init__(self, ingredients_repository: IngredientsRepository) -> None:
        self.ingredients_repository = ingredients_repository

    def execute(self, ingredient: IngredientDTO) -> dict:
        ingredient_to_create = Ingredients(
            name=ingredient.name,
        )

        inserted_ingredient = self.ingredients_repository.create_ingredient(ingredient_to_create)

        return inserted_ingredient.__dict__
