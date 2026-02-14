from abc import ABC, abstractmethod

from injector import inject

from src.repository.dishes_repository import DishesRepository
from src.dto.dish import DishDTO


class GetDishUseCase(ABC):
    @abstractmethod
    def execute(self, dish_uuid: str) -> DishDTO:
        pass


class GetDishUseCaseImpl(GetDishUseCase):
    @inject
    def __init__(self, dishes_repository: DishesRepository) -> None:
        self.dishes_repository = dishes_repository

    def execute(self, dish_uuid: str) -> DishDTO:
        dish = self.dishes_repository.get_dish(dish_uuid)

        if not dish:
            raise ValueError("No dish with the supplied UUID was found in the database.")

        dish_dto = DishDTO(uuid=dish.uuid, name=dish.name)

        return dish_dto
