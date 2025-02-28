from unittest.mock import MagicMock, Mock

import pytest
from pika.spec import BasicProperties

from bababel.rabbitmq.rabbitmq_connection import RabbitMQConnection


@pytest.fixture(autouse=True)
def mock_conn(mocker):
    yield mocker.patch("bababel.rabbitmq.rabbitmq_connection.BlockingConnection", MagicMock())


class TestRabbitMQConnection:
    def setup_method(self):
        self.params = Mock()

    @pytest.fixture
    def sut(self):
        return RabbitMQConnection(parameters=self.params)

    def test_queue_declare(self, sut):
        args = ['arg1', 'arg2']
        kwargs = {
            'kwarg1': 'value1',
            'kwarg2': 'value2'
        }
        response = sut.queue_declare(*args, **kwargs)

        sut.channel.queue_declare.assert_called_once_with(*args, **kwargs)
        assert response == sut.channel.queue_declare.return_value

    def test_basic_consume(self, sut):
        args = ['arg1', 'arg2']
        kwargs = {
            'kwarg1': 'value1',
            'kwarg2': 'value2'
        }
        response = sut.basic_consume(*args, **kwargs)

        sut.channel.basic_consume.assert_called_once_with(*args, **kwargs)
        assert response == sut.channel.basic_consume.return_value

    def test_start_consuming(self, sut):
        response = sut.start_consuming()

        sut.channel.start_consuming.assert_called_once_with()
        assert response == sut.channel.start_consuming.return_value

    def test_process_events(self, sut):
        sut.process_events()

        sut.conn.process_data_events.assert_called_once_with()

    def test_publish(self, sut):
        prop = BasicProperties()
        sut.publish(exchange='xpto', routing_key='xpto2', body='xpto3', properties=prop)

        sut.channel.basic_publish.assert_called_once_with(exchange='xpto', routing_key='xpto2', body='xpto3',
                                                          properties=prop)

    def test_declare_exchange(self, sut):
        sut.declare_exchange(exchange='xpto')

        sut.channel.exchange_declare.assert_called_once_with(exchange='xpto')
