from abc import ABC, abstractmethod
from common.dtos import UserAuthTokensDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def get_response_for_login(self,
                               user_token_dto: UserAuthTokensDTO,
                               is_admin: bool):
        pass
