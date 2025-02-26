# Standard Library
from abc import ABC, abstractmethod
import uuid


class Utils(ABC):
    @abstractmethod
    def invalid_uuid(self, uuid_to_test) -> bool:
        pass


class UtilsImpl(Utils):
    def __init__(self):
        pass

    def invalid_uuid(self, uuid_to_test) -> bool:
        try:
            uuid.UUID(uuid_to_test, version=4)
        except ValueError:
            return True
        return False
