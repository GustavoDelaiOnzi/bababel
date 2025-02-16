import pytest

from bababel.rabbitmq.client import RabbitMQClient


@pytest.fixture(autouse=True)
def mock_credentials(mocker):
    return mocker.patch("bababel.rabbitmq.client.PlainCredentials")


@pytest.fixture(autouse=True)
def mock_conn_params(mocker):
    return mocker.patch("bababel.rabbitmq.client.ConnectionParameters")


@pytest.fixture(autouse=True)
def mock_conn(mocker):
    return mocker.patch("bababel.rabbitmq.client.RabbitMQConnection")


class TestRabbitMQClient:
    def setup_method(self, ):
        self.host = 'host'
        self.port = 1234
        self.username = 'username'
        self.password = 'password'

    @pytest.fixture
    def sut(self):
        return RabbitMQClient()

    @pytest.fixture(autouse=True)
    def sut_connect(self, sut):
        yield sut.connect(host=self.host, port=self.port, username=self.username, password=self.password)

    def test_should_return_connection(self, sut_connect, mock_conn):
        # GIVEN
        # WHEN
        # THEN
        assert sut_connect == mock_conn.return_value

    def test_should_call_connection_with_correct_params(self, mock_conn, mock_conn_params):
        # GIVEN
        # WHEN
        # THEN
        mock_conn.assert_called_once_with(parameters=mock_conn_params.return_value)


    def test_should_call_connection_parameters_with_correct_params(self, mock_credentials):
        # GIVEN
        # WHEN
        # THEN
        mock_credentials.assert_called_once_with(username=self.username, password=self.password)

    def test_should_call_credentials_with_correct_params(self, mock_conn_params, mock_credentials):
        # GIVEN
        # WHEN
        # THEN
        mock_conn_params.assert_called_once_with(host=self.host, port=self.port,
                                                 credentials=mock_credentials.return_value)
