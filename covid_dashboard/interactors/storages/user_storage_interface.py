from abc import ABC, abstractmethod


class UserStorageInterface(ABC):

    @abstractmethod
    def is_valid_username(self, username: str):
        pass

    @abstractmethod
    def is_valid_password(self, username: str, password: int) -> int:
        pass

    @abstractmethod
    def is_user_admin(self, user_id: int) -> bool:
        pass