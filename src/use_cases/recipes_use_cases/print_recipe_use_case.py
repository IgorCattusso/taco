from abc import ABC, abstractmethod

from injector import inject


class PrintRecipeUseCase(ABC):
    @abstractmethod
    def execute(self, card_comment: dict) -> list:
        pass


class PrintRecipeUseCaseImpl(PrintRecipeUseCase):
    @inject
    def __init__(
            self,
            a: 123,
    ) -> None:
        self.a = a

    def execute(self, card_comment: dict) -> list:
        ...
