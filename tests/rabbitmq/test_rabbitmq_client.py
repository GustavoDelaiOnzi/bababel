import pytest

from bababel.rabbitmq.rabbitmq_client import RabbitMQClient


@pytest.fixture(autouse=True)
def mock_credentials(mocker):
    return mocker.patch("bababel.rabbitmq.rabbitmq_client.PlainCredentials")


@pytest.fixture(autouse=True)
def mock_conn_params(mocker):
    return mocker.patch("bababel.rabbitmq.rabbitmq_client.ConnectionParameters")


@pytest.fixture(autouse=True)
def mock_conn(mocker):
    return mocker.patch("bababel.rabbitmq.rabbitmq_client.RabbitMQConnection")


class TestRabbitMQClient:
    def setup_method(self):
        self.host = 'host'
        self.port = 1234
        self.username = 'username'
        self.password = 'password'

    @pytest.fixture
    def sut(self):
        return RabbitMQClient()

    def test_connect(self, sut, mock_conn, mock_conn_params, mock_credentials):
        response = sut.connect(host=self.host, port=self.port, username=self.username, password=self.password)

        assert response == mock_conn.return_value
        mock_conn.assert_called_once_with(parameters=mock_conn_params.return_value)
        mock_credentials.assert_called_once_with(username=self.username, password=self.password)
        mock_conn_params.assert_called_once_with(host=self.host, port=self.port,
                                                 credentials=mock_credentials.return_value)
