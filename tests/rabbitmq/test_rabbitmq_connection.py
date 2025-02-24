from unittest.mock import Mock, MagicMock

import pytest

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
