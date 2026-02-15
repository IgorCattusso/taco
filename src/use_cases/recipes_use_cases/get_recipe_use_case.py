from abc import ABC, abstractmethod

from injector import inject

from src.repository.recipes_repository import RecipesRepository
from src.dto.recipe import RecipeDTO


class GetRecipeUseCase(ABC):
    @abstractmethod
    def execute(self, recipe_uuid: str) -> RecipeDTO:
        pass


class GetRecipeUseCaseImpl(GetRecipeUseCase):
    @inject
    def __init__(self, recipes_repository: RecipesRepository) -> None:
        self.recipes_repository = recipes_repository

    def execute(self, recipe_uuid: str) -> RecipeDTO:
        recipe = self.recipes_repository.get_recipe(recipe_uuid)

        if not recipe:
            raise ValueError("No recipe with the supplied UUID was found in the database.")

        recipe_dto = RecipeDTO(
            uuid=recipe.uuid,
            dish_uuid=recipe.dish_uuid,
            nutritional_value_uuid=recipe.nutritional_value__uuid,
            quantity=recipe.quantity,
        )

        return recipe_dto
