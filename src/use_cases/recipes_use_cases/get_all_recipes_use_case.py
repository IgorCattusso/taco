from abc import ABC, abstractmethod

from injector import inject

from src.repository.recipes_repository import RecipesRepository
from src.dto.recipe import RecipeDTO


class GetAllRecipesUseCase(ABC):
    @abstractmethod
    def execute(self) -> list[RecipeDTO]:
        pass


class GetAllRecipesUseCaseImpl(GetAllRecipesUseCase):
    @inject
    def __init__(self, recipes_repository: RecipesRepository) -> None:
        self.recipes_repository = recipes_repository

    def execute(self) -> list[RecipeDTO]:
        recipes = self.recipes_repository.get_all_recipes()

        if not recipes:
            raise ValueError("No recipes were found in the database.")

        recipes_dto = [
            RecipeDTO(
                uuid=recipe.uuid,
                dish_uuid=recipe.dish_uuid,
                nutritional_value_uuid=recipe.nutritional_value__uuid,
                quantity=recipe.quantity,
            ) for recipe in recipes
        ]

        return recipes_dto
