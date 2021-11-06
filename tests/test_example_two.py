import pytest


@pytest.fixture
def yield_fixture():
    print("yield_fixture")
    yield 6
    print("teardown")


def test_example_one(yield_fixture):
    print("test_example_one")
    assert yield_fixture == 6
