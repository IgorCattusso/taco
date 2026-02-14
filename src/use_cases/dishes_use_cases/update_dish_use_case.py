from abc import ABC, abstractmethod

from injector import inject

from src.repository.dishes_repository import DishesRepository
from src.dto.dish import Dish


class UpdateDishUseCase(ABC):
    @abstractmethod
    def execute(self, dish: dict) -> dict:
        pass


class UpdateDishUseCaseImpl(UpdateDishUseCase):
    @inject
    def __init__(self, dishes_repository: DishesRepository) -> None:
        self.dishes_repository = dishes_repository

    def execute(self, dish: Dish) -> dict:
        new_dish = self.dishes_repository.update_dish(dish)
        return new_dish.__dict__
