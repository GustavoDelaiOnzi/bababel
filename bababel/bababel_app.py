import nanoid


class BababelApp:
    def __init__(self, host: str, port: int, username: str, password: str):
        """TODO: Remove publisher from here maybe implementing singleton to remove circular import"""
        from bababel.publisher.publisher import Publisher
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.identifier = nanoid.generate()  # Exchange name for rabbitmq implementation
        self.publisher = Publisher(self)
