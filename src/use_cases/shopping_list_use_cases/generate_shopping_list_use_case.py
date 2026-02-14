from abc import ABC, abstractmethod

from injector import inject


class GenerateShoppingListUseCase(ABC):
    @abstractmethod
    def execute(self, card_comment: dict) -> list:
        pass


class GenerateShoppingListUseCaseImpl(GenerateShoppingListUseCase):
    @inject
    def __init__(
            self,
            a: 123,
    ) -> None:
        self.a = a

    def execute(self, card_comment: dict) -> list:
        ...
