from unittest.mock import MagicMock

import pytest

from bababel.consumer import Consumer


@pytest.fixture(autouse=True)
def mock_client(mocker):
    yield mocker.patch("bababel.consumer.RabbitMQClient", MagicMock())


class TestWorker:
    def setup_method(self):
        self.host = "host"
        self.port = 1234
        self.username = "username"
        self.password = "password"

    @pytest.fixture
    def sut(self):
        return Consumer(host=self.host, port=self.port, username=self.username, password=self.password)

    @pytest.fixture
    def mock_conn(self, mock_client):
        yield mock_client.return_value.connect

    @pytest.fixture
    def mock_channel(self, mock_conn):
        yield mock_conn.return_value.establish

    @pytest.fixture
    def mock_declare(self, mock_conn):
        yield mock_conn.return_value.queue_declare

    @pytest.fixture
    def mock_consume(self, mock_conn):
        yield mock_conn.return_value.basic_consume

    def test_should_connect(self, sut, binds, mock_conn):
        bind = binds[0]

        response = sut.declare_bind(queue_callback_bind=bind)

        assert sut.connection == mock_conn.return_value
        sut.connection.queue_declare.assert_called_once_with(queue=bind.queue, durable=True)
        sut.connection.basic_consume.assert_called_once_with(queue=bind.queue, on_message_callback=bind.callback)
        assert response is None

    def test_should_start(self, sut):
        response = sut.start()

        assert response is None
        sut.connection.process_events.assert_called_once_with()
