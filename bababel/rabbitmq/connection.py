from pika.adapters.blocking_connection import (BlockingChannel,
                                               BlockingConnection)
from pika.connection import ConnectionParameters
from pika.spec import BasicProperties


class RabbitMQConnection:
    def __init__(self, parameters: ConnectionParameters):
        self.conn: BlockingConnection = BlockingConnection(parameters=parameters)
        self.channel: BlockingChannel = self.conn.channel()

    def queue_declare(self, *args, **kwargs):
        return self.channel.queue_declare(*args, **kwargs)

    def basic_consume(self, *args, **kwargs):
        return self.channel.basic_consume(*args, **kwargs)

    def start_consuming(self):
        return self.channel.start_consuming()

    def process_events(self):
        return self.conn.process_data_events()

    def publish(self, exchange: str, routing_key: str, body: str | bytes, properties: BasicProperties = None):
        return self.channel.basic_publish(exchange=exchange,
                                          routing_key=routing_key,
                                          body=body,
                                          properties=properties)

    def declare_exchange(self, exchange: str):
        self.channel.exchange_declare(exchange=exchange)
