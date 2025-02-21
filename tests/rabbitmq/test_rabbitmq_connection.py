from unittest.mock import Mock

import pytest

from bababel.rabbitmq.rabbitmq_connection import RabbitMQConnection


@pytest.fixture(autouse=True)
def mock_conn(mocker):
    yield mocker.patch("bababel.rabbitmq.rabbitmq_connection.BlockingConnection")


@pytest.fixture(autouse=True)
def mock_channel(mock_conn):
    yield mock_conn.return_value.channel


class TestRabbitMQConnection:
    def setup_method(self):
        self.params = Mock()

    @pytest.fixture
    def sut(self):
        return RabbitMQConnection(parameters=self.params)

    def test_queue_declare(self, sut, mock_channel):
        # GIVEN
        args = ['arg1', 'arg2']
        kwargs = {
            'kwarg1': 'value1',
            'kwarg2': 'value2'
        }
        # WHEN
        response = sut.queue_declare(*args, **kwargs)

        # THEN
        mock_channel.return_value.queue_declare.assert_called_once_with(*args, **kwargs)
        assert response == mock_channel.return_value.queue_declare.return_value

    def test_basic_consume(self, sut, mock_channel):
        # GIVEN
        args = ['arg1', 'arg2']
        kwargs = {
            'kwarg1': 'value1',
            'kwarg2': 'value2'
        }
        # WHEN
        response = sut.basic_consume(*args, **kwargs)

        # THEN
        mock_channel.return_value.basic_consume.assert_called_once_with(*args, **kwargs)
        assert response == mock_channel.return_value.basic_consume.return_value

    def test_start_consuming(self, sut, mock_channel):
        # GIVEN
        # WHEN
        response = sut.start_consuming()

        # THEN
        mock_channel.return_value.start_consuming.assert_called_once_with()
        assert response == mock_channel.return_value.start_consuming.return_value
