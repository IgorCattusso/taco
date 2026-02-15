from abc import ABC, abstractmethod

from injector import inject

from src.repository.preparation_method_repository import PreparationMethodsRepository
from src.entities.preparation_method import PreparationMethod
from src.dto.preparation_method import PreparationMethodDTO


class UpdatePreparationMethodUseCase(ABC):
    @abstractmethod
    def execute(self, preparation_method_uuid: str, preparation_method: PreparationMethodDTO) -> dict:
        pass


class UpdatePreparationMethodUseCaseImpl(UpdatePreparationMethodUseCase):
    @inject
    def __init__(self, preparation_methods_repository: PreparationMethodsRepository) -> None:
        self.preparation_methods_repository = preparation_methods_repository

    def execute(self, preparation_method_uuid: str, preparation_method: PreparationMethodDTO) -> dict:
        preparation_method_to_update = PreparationMethod(
            uuid=preparation_method_uuid,
            dish_uuid=preparation_method.dish_uuid,
            preparation_method=preparation_method.preparation_method,
        )

        updated_preparation_method = \
            self.preparation_methods_repository.update_preparation_method(preparation_method_to_update)

        preparation_method_dto = PreparationMethodDTO(
            uuid=updated_preparation_method.uuid,
            dish_uuid=updated_preparation_method.dish_uuid,
            preparation_method=updated_preparation_method.preparation_method,
        )

        return preparation_method_dto.__dict__
