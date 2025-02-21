# Standard Library
from abc import ABC, abstractmethod

# Third-Party Libraries
from injector import inject

# Project-specific Modules


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
