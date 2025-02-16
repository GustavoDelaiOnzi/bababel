from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def establish(self): ...  # TODO add Channel interface
