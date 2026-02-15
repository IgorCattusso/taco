from abc import ABC, abstractmethod

from injector import inject

from src.repository.recipes_repository import RecipesRepository
from src.entities.recipes import Recipe
from src.dto.recipe import RecipeDTO


class UpdateRecipeUseCase(ABC):
    @abstractmethod
    def execute(self, recipe_uuid: str, recipe: RecipeDTO) -> dict:
        pass


class UpdateRecipeUseCaseImpl(UpdateRecipeUseCase):
    @inject
    def __init__(self, recipes_repository: RecipesRepository) -> None:
        self.recipes_repository = recipes_repository

    def execute(self, recipe_uuid: str, recipe: RecipeDTO) -> dict:
        recipe_to_update = Recipe(
            uuid=recipe_uuid,
            dish_uuid=recipe.dish_uuid,
            nutritional_value__uuid=recipe.nutritional_value_uuid,
            quantity=recipe.quantity,
        )

        updated_recipe = self.recipes_repository.update_recipe(recipe_to_update)

        recipe_dto = RecipeDTO(
            uuid=updated_recipe.uuid,
            dish_uuid=updated_recipe.dish_uuid,
            nutritional_value_uuid=updated_recipe.nutritional_value__uuid,
            quantity=updated_recipe.quantity,
        )

        return recipe_dto.__dict__
