# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject

# Project-specific Modules
from src.repository.recipes_repository import RecipesRepository


class GetRecipeUseCase(ABC):
    @abstractmethod
    def execute(self, recipe_uuid: str) -> dict:
        pass


class GetRecipeUseCaseImpl(GetRecipeUseCase):
    @inject
    def __init__(
        self,
        recipes_repository: RecipesRepository,
    ) -> None:
        self.recipes_repository = recipes_repository

    def execute(self, recipe_uuid: str) -> dict:
        recipe = self.recipes_repository.get_recipe_by_uuid(recipe_uuid)
        return {
            recipe.uuid: {
                "dish_uuid": recipe.dish_uuid,
                "nutritional_value_uuid": recipe.nutritional_value__uuid,
                "amount": recipe.amount,
            }
        }
        