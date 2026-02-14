from abc import ABC, abstractmethod

from injector import inject

from src.repository.preparation_method_repository import PreparationMethodsRepository


class DeletePreparationMethodUseCase(ABC):
    @abstractmethod
    def execute(self, preparation_method_uuid: str) -> dict:
        pass


class DeletePreparationMethodhUseCaseImpl(DeletePreparationMethodUseCase):
    @inject
    def __init__(self, preparation_method: PreparationMethodsRepository) -> None:
        self.preparation_method = preparation_method

    def execute(self, preparation_method_uuid: str) -> dict:
        self.preparation_method.delete_preparation_method(preparation_method_uuid)

        return 'Preparation method deleted successfully.'
