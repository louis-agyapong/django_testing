import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test_user")


@pytest.mark.django_db
def test_set_password(user_1):
    user_1.set_password("test_password")
    assert user_1.check_password("test_passwords") is True
