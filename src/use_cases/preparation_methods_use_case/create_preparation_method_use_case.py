from abc import ABC, abstractmethod

from injector import inject

from src.repository.preparation_method_repository import PreparationMethodsRepository
from src.entities.preparation_method import PreparationMethod
from src.dto.preparation_method import PreparationMethodDTO


class CreatePreparationMethodUseCase(ABC):
    @abstractmethod
    def execute(self, preparation_method: PreparationMethodDTO) -> dict:
        pass


class CreatePreparationMethodUseCaseImpl(CreatePreparationMethodUseCase):
    @inject
    def __init__(self, preparation_methods_repository: PreparationMethodsRepository) -> None:
        self.preparation_methods_repository = preparation_methods_repository

    def execute(self, preparation_method: PreparationMethodDTO) -> dict:
        preparation_method_to_create = PreparationMethod(
            dish_uuid=preparation_method.dish_uuid,
            preparation_method=preparation_method.preparation_method,
        )

        inserted_preparation_method = \
            self.preparation_methods_repository.create_preparation_method(preparation_method_to_create)

        return inserted_preparation_method.__dict__
