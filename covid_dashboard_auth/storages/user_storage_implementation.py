from covid_dashboard_auth.exceptions.exceptions import \
    InvalidUsername, InvalidPassword
from covid_dashboard_auth.interactors.storages.dtos import \
    UserDetailsDTO
from covid_dashboard_auth.models import User
from covid_dashboard_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface


class UserStorageImplementation(UserStorageInterface): 

    def is_valid_username(self, username: str):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername

    def is_valid_password(self, username: str, password: str) -> int:

        user = User.objects.get(username=username)

        is_password_valid = user.check_password(password)
        is_invalid_password = not is_password_valid

        if is_invalid_password:
            raise InvalidPassword

        return user.id

    def get_user_details_dto(self, user_id: int) -> UserDetailsDTO:
        user = User.objects.get(id=user_id)
        user_details_dto = self._convert_user_object_to_dto(user=user)
        return user_details_dto

    @staticmethod
    def _convert_user_object_to_dto(user):
        return UserDetailsDTO(
            user_id=user.id,
            is_admin=user.is_admin
        )
