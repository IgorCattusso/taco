# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject

# Project-specific Modules
from src.repository.dishes_repository import DishesRepository


class GetAllDishesUseCase(ABC):
    @abstractmethod
    def execute(self) -> dict:
        pass


class GetAllDishesUseCaseImpl(GetAllDishesUseCase):
    @inject
    def __init__(self, dishes_repository: DishesRepository) -> None:
        self.dishes_repository = dishes_repository

    def execute(self) -> dict:
        dishes = self.dishes_repository.get_all_dishes()

        if not dishes:
            raise ValueError("No dishes were found in the database.")

        return {"dishes": [{"dish_uuid": dish.uuid, "dish_name": dish.name} for dish in dishes]}
