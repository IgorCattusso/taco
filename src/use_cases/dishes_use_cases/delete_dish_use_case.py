from abc import ABC, abstractmethod

from injector import inject

from src.repository.dishes_repository import DishesRepository
from src.repository.preparation_method_repository import PreparationMethodsRepository
from src.repository.recipes_repository import RecipesRepository


class DeleteDishUseCase(ABC):
    @abstractmethod
    def execute(self, dish_uuid: str) -> dict:
        pass


class DeleteDishUseCaseImpl(DeleteDishUseCase):
    @inject
    def __init__(self,
                 dishes_repository: DishesRepository,
                 preparation_method_repository: PreparationMethodsRepository,
                 recipes_repository: RecipesRepository,
            ) -> None:
        self.dishes_repository = dishes_repository
        self.preparation_method = preparation_method_repository
        self.recipes = recipes_repository

    def execute(self, dish_uuid: str) -> dict:

        preparation_method = self.preparation_method.get_dish_preparation_method(dish_uuid)

        if preparation_method:
            self.preparation_method.delete_preparation_method(preparation_method.uuid)
        self.recipes.delete_recipe_by_dish_uuid(dish_uuid)
        self.dishes_repository.delete_dish(dish_uuid)

        return "Dish deleted successfully."
