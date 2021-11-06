import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test_user")
    return user


def test_user_1(user_1):
    assert user_1.username == "test_user"


def test_set_check_password(user_1):
    user_1.set_password("test_password")
    assert user_1.check_password("test_password") is True
