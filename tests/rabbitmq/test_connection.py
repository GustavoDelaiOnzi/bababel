from unittest.mock import Mock

import pytest

from bababel.rabbitmq.connection import RabbitMQConnection


@pytest.fixture(autouse=True)
def mock_conn(mocker):
    yield mocker.patch("bababel.rabbitmq.connection.BlockingConnection")


class TestRabbitMQConnection:
    def setup_method(self):
        self.params = Mock()

    @pytest.fixture
    def sut(self):
        return RabbitMQConnection(parameters=self.params)

    def test_should_return_connection(self, sut, mock_conn):
        # GIVEN
        # WHEN
        sut.establish()
        # THEN
        mock_conn.assert_called_once_with(parameters=self.params)
