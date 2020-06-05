from covid_dashboard.exceptions.exceptions import \
    InvalidUsername, InvalidPassword
from covid_dashboard.interactors.storages.dtos import \
    UserDetailsDto
from covid_dashboard.models import User
from covid_dashboard.interactors.storages.user_storage_interface import \
    UserStorageInterface


class UserStorageImplementation(UserStorageInterface): 

    def is_valid_username(self, username: str):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername

        return

    def is_valid_password(self, username: str, password: str) \
        -> UserDetailsDto:
        user = User.objects.get(username=username)

        is_password_valid = user.check_password(password)
        is_invalid_password = not is_password_valid

        if is_invalid_password:
            raise InvalidPassword

        user_details_dto = UserDetailsDto(
            user_id=user.id,
            is_admin=user.is_admin
        )

        return user_details_dto

    def is_user_admin(self, user_id: int):
        user = User.objects.get(id=user_id)
        return user.is_admin
