import pytest

from bababel import Worker


@pytest.fixture(autouse=True)
def mock_client(mocker):
    yield mocker.patch("bababel.worker.worker.RabbitMQClient")


class TestWorker:
    def setup_method(self):
        self.host = "host"
        self.port = 1234
        self.username = "username"
        self.password = "password"

    @pytest.fixture
    def sut(self):
        return Worker(host=self.host, port=self.port, username=self.username, password=self.password)

    @pytest.fixture
    def mock_conn(self, mock_client):
        yield mock_client.return_value.connect

    @pytest.fixture
    def mock_channel(self, mock_conn):
        yield mock_conn.return_value.establish

    def test_should_connect(self, sut, binds, mock_conn):
        # GIVEN
        bind = binds[0]
        # WHEN
        sut.consume_bind(queue_callback_bind=bind)
        # THEN
        assert sut.connection == mock_conn.return_value

    def test_should_declare_queue_with_correct_params(self, sut, binds, mock_conn):
        # GIVEN
        mock_declare = mock_conn.return_value.queue_declare
        bind = binds[0]
        # WHEN
        sut.consume_bind(queue_callback_bind=bind)
        # THEN
        mock_declare.assert_called_once_with(queue=bind.queue, durable=True)

    def test_should_basic_consume_with_correct_params(self, sut, binds, mock_conn):
        # GIVEN
        mock_basic_consume = mock_conn.return_value.basic_consume
        bind = binds[0]
        # WHEN
        sut.consume_bind(queue_callback_bind=bind)
        # THEN
        mock_basic_consume.assert_called_once_with(queue=bind.queue, on_message_callback=bind.callback)

    def test_should_start_consuming(self, sut, binds, mock_conn):
        # GIVEN
        mock_start_consuming = mock_conn.return_value.start_consuming
        bind = binds[0]
        # WHEN
        sut.consume_bind(queue_callback_bind=bind)
        # THEN
        mock_start_consuming.assert_called_once_with()

    def test_should_return_none_on_consume(self, sut, binds):
        # GIVEN
        bind = binds[0]
        # WHEN
        response = sut.consume_bind(queue_callback_bind=bind)
        # THEN
        assert response is None
