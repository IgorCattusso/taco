from abc import ABC


class Utils(ABC):
    def some_function(self) -> str:
        ...


class UtilsImpl(Utils):
    def __init__(self):
        ...

    def some_function(self) -> str:
        ...
