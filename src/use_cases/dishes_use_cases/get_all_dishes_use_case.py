from abc import ABC, abstractmethod

from injector import inject

from src.repository.dishes_repository import DishesRepository
from src.dto.dish import DishDTO


class GetAllDishesUseCase(ABC):
    @abstractmethod
    def execute(self) -> list[DishDTO]:
        pass


class GetAllDishesUseCaseImpl(GetAllDishesUseCase):
    @inject
    def __init__(self, dishes_repository: DishesRepository) -> None:
        self.dishes_repository = dishes_repository

    def execute(self) -> list[DishDTO]:
        dishes = self.dishes_repository.get_all_dishes()

        if not dishes:
            raise ValueError("No dishes were found in the database.")

        dishes_dto = [
            DishDTO(
                uuid=dish.uuid,
                name=dish.name
            ) for dish in dishes
        ]

        return dishes_dto
