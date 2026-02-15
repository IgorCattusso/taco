from abc import ABC, abstractmethod

from injector import inject

from src.repository.recipes_repository import RecipesRepository
from src.entities.recipes import Recipe
from src.dto.recipe import RecipeDTO


class CreateRecipeUseCase(ABC):
    @abstractmethod
    def execute(self, recipe: RecipeDTO) -> dict:
        pass


class CreateRecipeUseCaseImpl(CreateRecipeUseCase):
    @inject
    def __init__(self, recipes_repository: RecipesRepository) -> None:
        self.recipes_repository = recipes_repository

    def execute(self, recipe: RecipeDTO) -> dict:
        recipe_to_create = Recipe(
            dish_uuid=recipe.dish_uuid,
            nutritional_value__uuid=recipe.nutritional_value_uuid,
            quantity=recipe.quantity,
        )

        inserted_recipe = self.recipes_repository.create_recipe(recipe_to_create)

        return inserted_recipe.__dict__
