# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject

# Project-specific Modules
from src.repository.recipes_repository import RecipesRepository


class GetRecipeByDishUuidUseCase(ABC):
    @abstractmethod
    def execute(self, dish_uuid: str) -> dict:
        pass


class GetRecipeByDishUuidUseCaseImpl(GetRecipeByDishUuidUseCase):
    @inject
    def __init__(self, recipes_repository: RecipesRepository,) -> None:
        self.recipes_repository = recipes_repository

    def execute(self, dish_uuid: str) -> dict:
        recipe = self.recipes_repository.get_recipe_by_dish_uuid(dish_uuid)
        ingredients = {
            ingredient.uuid: {
                "ingredient_uuid": ingredient.uuid,
                "ingredient_name": ingredient.ingredient_name,
                "measurement_unit": ingredient.measurement_unit,
                "amount": ingredient.amount,
            }
            for ingredient in recipe
        }

        return {
            "dish_uuid": dish_uuid,
            "dish_name": recipe[0].dish_name,
            "ingredients": ingredients
        }
