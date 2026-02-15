from abc import ABC, abstractmethod

from injector import inject

from src.repository.ingredients_repository import IngredientsRepository
from src.entities.ingredients import Ingredients
from src.dto.ingredient import IngredientDTO


class UpdateIngredientUseCase(ABC):
    @abstractmethod
    def execute(self, ingredient_uuid: str, ingredient: dict) -> dict:
        pass


class UpdateIngredientUseCaseImpl(UpdateIngredientUseCase):
    @inject
    def __init__(self, ingredients_repository: IngredientsRepository) -> None:
        self.ingredients_repository = ingredients_repository

    def execute(self, ingredient_uuid: str, ingredient: IngredientDTO) -> dict:
        ingredient_to_update = Ingredients(
            uuid=ingredient_uuid,
            name=ingredient.name,
        )

        updated_ingredient = self.ingredients_repository.update_ingredient(ingredient_to_update)

        ingredient_dto = IngredientDTO(
            uuid=updated_ingredient.uuid,
            name=updated_ingredient.name,
        )

        return ingredient_dto.__dict__
