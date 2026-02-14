from abc import ABC, abstractmethod

from injector import inject

from src.repository.dishes_repository import DishesRepository
from src.entities.dishes import Dishes
from src.dto.dish import DishDTO


class CreateDishUseCase(ABC):
    @abstractmethod
    def execute(self, dish: dict) -> dict:
        pass


class CreateDishUseCaseImpl(CreateDishUseCase):
    @inject
    def __init__(self, dishes_repository: DishesRepository) -> None:
        self.dishes_repository = dishes_repository

    def execute(self, dish: DishDTO) -> dict:
        dish_to_create = Dishes(
            name=dish.name,
        )

        inserted_dish = self.dishes_repository.create_dish(dish_to_create)

        return inserted_dish.__dict__
