from pytest import fixture

from test.utils.fake_session import FakeSession


@fixture
def fake_session():
    return FakeSession()

