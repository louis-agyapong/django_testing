import pytest
from django.contrib.auth.models import User


"""
Note:
The first test returns 1 the second test returns 0.
That confirms that the table in the first test doesn't
persist over to the next test.
"""


@pytest.mark.django_db
def test_user_create():
    """
    The first test is to check if the user is created.
    """
    user = User.objects.create_user(
        username="test",
        email="test@mail.com",
        password="test",
    )
    count = User.objects.all().count()
    print(count)
    count == 1
    assert user.username == "test"


@pytest.mark.django_db
def test_user_objects():
    count = User.objects.all().count()
    print(count)
    assert count == 0
