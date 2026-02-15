from abc import ABC, abstractmethod

from injector import inject

from src.repository.recipes_repository import RecipesRepository


class DeleteRecipeUseCase(ABC):
    @abstractmethod
    def execute(self, recipe_uuid: str) -> dict:
        pass


class DeleteRecipeUseCaseImpl(DeleteRecipeUseCase):
    @inject
    def __init__(self, recipes_repository: RecipesRepository) -> None:
        self.recipes_repository = recipes_repository

    def execute(self, recipe_uuid: str) -> dict:
        self.recipes_repository.delete_recipe(recipe_uuid)

        return "Recipe deleted successfully."
