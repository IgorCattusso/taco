from abc import ABC, abstractmethod

from injector import inject

from src.repository.preparation_method_repository import PreparationMethodsRepository
from src.dto.preparation_method import PreparationMethodDTO


class GetPreparationMethodUseCase(ABC):
    @abstractmethod
    def execute(self, preparation_method_uuid: str) -> PreparationMethodDTO:
        pass


class GetPreparationMethodUseCaseImpl(GetPreparationMethodUseCase):
    @inject
    def __init__(self, preparation_methods_repository: PreparationMethodsRepository) -> None:
        self.preparation_methods_repository = preparation_methods_repository

    def execute(self, preparation_method_uuid: str) -> PreparationMethodDTO:
        preparation_method = self.preparation_methods_repository.get_preparation_method(preparation_method_uuid)

        if not preparation_method:
            raise ValueError("No preparation method with the supplied UUID was found in the database.")

        preparation_method_dto = PreparationMethodDTO(
            uuid=preparation_method.uuid,
            dish_uuid=preparation_method.dish_uuid,
            preparation_method=preparation_method.preparation_method,
        )

        return preparation_method_dto
