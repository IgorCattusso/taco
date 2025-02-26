# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject

# Project-specific Modules
from src.repository.preparation_method_repository import PreparationMethodsRepository


class GetPreparationMethodByDishUuidUseCase(ABC):
    @abstractmethod
    def execute(self, dish_uuid: str) -> str:
        pass


class GetPreparationMethodByDishUuidUseCaseImpl(GetPreparationMethodByDishUuidUseCase):
    @inject
    def __init__(self, preparation_methods_repository: PreparationMethodsRepository) -> None:
        self.preparation_methods_repository = preparation_methods_repository

    def execute(self, dish_uuid: str) -> str:
        preparation_method = self.preparation_methods_repository.get_dish_preparation_method(dish_uuid)
        if preparation_method:
            return preparation_method.preparation_method

        raise ValueError('The provided uuid was not found in the database.')
