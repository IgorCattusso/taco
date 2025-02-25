# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject

# Project-specific Modules
from src.repository.ingredients_repository import IngredientsRepository


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
        all_ingredients = {"ingredients": []}
        for ingredient in ingredients:
            all_ingredients["ingredients"].append(
                {
                    "dish_uuid": ingredient.uuid,
                    "dish_name": ingredient.name
                }
            )

        return all_ingredients
