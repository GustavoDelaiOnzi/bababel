import pytest

from bababel.app import BababelApp


@pytest.fixture(autouse=True)
def mock_publisher(mocker):
    yield mocker.patch('bababel.app.MessageRouter')


@pytest.fixture(autouse=True)
def mock_client(mocker):
    yield mocker.patch('bababel.app.RabbitMQClient')


class TestBababelApp:
    @pytest.fixture
    def sut(self):
        return BababelApp(host='host',
                          port=1,
                          username='xpto',
                          password='xpto')

    def test_should_init(self, sut):
        pass
