from abc import ABC, abstractmethod

from bababel.abstracts.connection import IConnection


class IClient(ABC):
    """
    Interface for a client that connects to a remote server.
    """
    @abstractmethod
    def connect(self, host: str, port: int, username: str, password: str) -> IConnection:
        """
        Establish a connection to the specified host.
        Args:
            host (str): The hostname or IP address of the server to connect to.
            port (int): The port number on which the server is listening.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        raise NotImplementedError()
