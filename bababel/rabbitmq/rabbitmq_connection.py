from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from pika.connection import ConnectionParameters

from bababel.abstracts.connection import Connection


class RabbitMQConnection(Connection):
    def __init__(self, parameters: ConnectionParameters):
        self.conn: BlockingConnection = BlockingConnection(parameters=parameters)
        self.channel: BlockingChannel = self.conn.channel()

    def queue_declare(self, *args, **kwargs):
        return self.channel.queue_declare(*args, **kwargs)

    def basic_consume(self, *args, **kwargs):
        return self.channel.basic_consume(*args, **kwargs)

    def start_consuming(self):
        return self.channel.start_consuming()
