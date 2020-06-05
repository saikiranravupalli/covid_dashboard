import pytest

from covid_dashboard.models import User
from covid_dashboard.storages.user_storage_implementation import \
    UserStorageImplementation

@pytest.mark.django_db
def test_is_valid_user_admin_given_invalid_user_as_admin_returns_false(user):

    # Arrange
    user_id = 1
    storage = UserStorageImplementation()

    # Act
    is_user_admin = storage.is_user_admin(user_id=user_id)

    # Assert
    assert is_user_admin is False

@pytest.mark.django_db
def test_is_valid_user_admin_given_invalid_user_as_admin_returns_true(superuser):

    # Arrange
    user_id = 1
    storage = UserStorageImplementation()

    # Act
    is_user_admin = storage.is_user_admin(user_id=user_id)

    # Assert
    assert is_user_admin is True
