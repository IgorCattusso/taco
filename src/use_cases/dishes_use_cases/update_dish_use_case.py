from abc import ABC, abstractmethod

from injector import inject

from src.repository.dishes_repository import DishesRepository
from src.entities.dishes import Dishes
from src.dto.dish import DishDTO


class UpdateDishUseCase(ABC):
    @abstractmethod
    def execute(self, dish_uuid: str, dish: dict) -> dict:
        pass


class UpdateDishUseCaseImpl(UpdateDishUseCase):
    @inject
    def __init__(self, dishes_repository: DishesRepository) -> None:
        self.dishes_repository = dishes_repository

    def execute(self, dish_uuid: str, dish: DishDTO) -> dict:
        dish_to_update = Dishes(
            uuid=dish_uuid,
            name=dish.name,
        )

        updated_dish = self.dishes_repository.update_dish(dish_to_update)

        dish_dto = DishDTO(
            uuid=updated_dish.uuid,
            name=updated_dish.name,
        )

        return dish_dto.__dict__
