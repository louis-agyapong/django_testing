import pytest


@pytest.fixture(scope="module")
def fixture_one():
    print("run fixture one 🛠👨🏾‍🔧")
    return 1


def test_example_two(fixture_one):
    print("run test example two 🧪🔬")
    num = fixture_one
    assert num == 1


def test_example_three(fixture_one):
    print("run test example three 🧪🔬")
    num = fixture_one
    assert num == 1


def test_example_four(fixture_one):
    print("run test example four 🧪🔬")
    num = fixture_one
    assert num == 1


@pytest.mark.xfail
def test_example():
    assert 1 == 1


@pytest.mark.slow
def test_example_one():
    assert 2 == 2
