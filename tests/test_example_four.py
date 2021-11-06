import pytest
from django.contrib.auth.models import User

"""
Arrange, Act, Assert
Arrange: Create the test data. We are using the fixture to
arrange the data for the test.
Act: Run the test. Set the password for that user.
Assert: Check the results. Check that the new password matches
the password.
"""


@pytest.fixture()
def user_1(db):
    """
    Arrange: Create the test data. We are using the fixture to
    arrange the data for the test.
    """
    return User.objects.create_user("test_user")


@pytest.mark.django_db
def test_set_password(user_1):
    """
    Act: Run the test. Set the password for that user.
    """
    user_1.set_password("test_password")
    """
    Assert: Check the results. Check that the new password matches
    the password.
    """
    assert user_1.check_password("test_passwords") is True
