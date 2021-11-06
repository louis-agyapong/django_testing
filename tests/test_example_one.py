import pytest


@pytest.mark.xfail
def test_example():
    assert 1 == 1


@pytest.mark.slow
def test_example_one():
    assert 2 == 2
