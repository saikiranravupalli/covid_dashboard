import pytest
from covid_dashboard_auth.models import User
from covid_dashboard_auth.exceptions.exceptions import InvalidPassword
from covid_dashboard_auth.storages.user_storage_implementation import \
    UserStorageImplementation

@pytest.mark.django_db
def test_is_valid_user_password_with_invalid_details_raises_error(user):
    # Arrange
    username = 'user_1'
    password = ''
    storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidPassword):
        storage.is_valid_password(username=username, password=password)

@pytest.mark.django_db
def test_is_valid_password_with_valid_details_returns_user_details_dto(user):

    # Arrange
    username = 'user_1'
    password = 'password'
    storage = UserStorageImplementation()
    expected_user_id = 1

    # Act
    user_id = storage.is_valid_password(
        username=username,
        password=password
    )

    # Assert
    assert user_id == expected_user_id
