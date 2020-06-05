import pytest
from covid_dashboard.models import User
from covid_dashboard.exceptions.exceptions import InvalidPassword
from covid_dashboard.storages.user_storage_implementation import \
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
def test_is_valid_password_with_valid_details_returns_user_details_dto(
    user, user_dto):

    # Arrange
    username = 'user_1'
    password = 'password'
    storage = UserStorageImplementation()
    expected_dto = user_dto

    # Act
    user_details_dto = storage.is_valid_password(
        username=username,
        password=password
    )

    # Assert
    assert user_details_dto == expected_dto