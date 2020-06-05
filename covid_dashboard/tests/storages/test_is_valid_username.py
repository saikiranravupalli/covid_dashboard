import pytest
from covid_dashboard.models import User
from covid_dashboard.exceptions.exceptions import InvalidUsername
from covid_dashboard.storages.user_storage_implementation import \
    UserStorageImplementation

@pytest.mark.django_db
def test_is_valid_username_with_invalid_details_raises_error():
    # Arrange
    invalidusername = ''
    storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUsername):
        storage.is_valid_username(username=invalidusername)

@pytest.mark.django_db
def test_is_valid_username_with_valid_details(user):
    # Arrange
    username = 'user_1'
    storage = UserStorageImplementation()
    storage.is_valid_username(
        username=username
    )

    # Act
    user = User.objects.get(username=username)

    # Assert
    assert user.username == username
