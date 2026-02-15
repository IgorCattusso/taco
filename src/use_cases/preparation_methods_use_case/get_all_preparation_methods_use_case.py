from abc import ABC, abstractmethod

from injector import inject

from src.repository.preparation_method_repository import PreparationMethodsRepository
from src.dto.preparation_method import PreparationMethodDTO


class GetAllPreparationMethodsUseCase(ABC):
    @abstractmethod
    def execute(self) -> list[PreparationMethodDTO]:
        pass


class GetAllPreparationMethodsUseCaseImpl(GetAllPreparationMethodsUseCase):
    @inject
    def __init__(self, preparation_methods_repository: PreparationMethodsRepository) -> None:
        self.preparation_methods_repository = preparation_methods_repository

    def execute(self) -> list[PreparationMethodDTO]:
        preparation_methods = self.preparation_methods_repository.get_all_preparation_methods()

        if not preparation_methods:
            raise ValueError("No preparation methods were found in the database.")

        preparation_methods_dto = [
            PreparationMethodDTO(
                uuid=preparation_method.uuid,
                dish_uuid=preparation_method.dish_uuid,
                preparation_method=preparation_method.preparation_method,
            ) for preparation_method in preparation_methods
        ]

        return preparation_methods_dto
