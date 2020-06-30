from abc import ABC, abstractmethod
from covid_dashboard_auth.interactors.storages.dtos import UserDetailsDTO


class UserStorageInterface(ABC):

    @abstractmethod
    def is_valid_username(self, username: str):
        pass

    @abstractmethod
    def is_valid_password(self, username: str, password: int) -> int:
        pass

    @abstractmethod
    def get_user_details_dto(self, user_id: int) -> UserDetailsDTO:
        pass
