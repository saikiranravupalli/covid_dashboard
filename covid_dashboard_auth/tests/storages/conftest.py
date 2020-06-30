import pytest
from covid_dashboard_auth.models import User
from covid_dashboard_auth.interactors.storages.dtos import UserDetailsDTO


@pytest.fixture()
def user():
    user = User.objects.create(
        username='user_1'
    )
    user.set_password('password')
    user.save()
    return user

@pytest.fixture()
def user_dto():
    user_dto = UserDetailsDTO(
        user_id=1,
        is_admin=False
    )
    return user_dto
