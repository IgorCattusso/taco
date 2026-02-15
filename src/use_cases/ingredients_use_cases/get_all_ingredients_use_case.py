from abc import ABC, abstractmethod

from injector import inject

from src.repository.ingredients_repository import IngredientsRepository
from src.dto.ingredient import IngredientDTO


class GetAllIngredientsUseCase(ABC):
    @abstractmethod
    def execute(self) -> dict:
        pass


class GetAllIngredientsUseCaseImpl(GetAllIngredientsUseCase):
    @inject
    def __init__(self, ingredients_repository: IngredientsRepository) -> None:
        self.ingredients_repository = ingredients_repository

    def execute(self) -> dict:
        ingredients = self.ingredients_repository.get_all_ingredients()

        if not ingredients:
            raise ValueError("No ingredients were found in the database.")

        ingredients_dto = [
            IngredientDTO(
                uuid=ingredient.uuid,
                name=ingredient.name
            ) for ingredient in ingredients
        ]

        return ingredients_dto
