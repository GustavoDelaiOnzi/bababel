from abc import ABC, abstractmethod


class IClient(ABC):
    @abstractmethod
    def connect(self, host: str, port: int, username: str, password: str): ...
