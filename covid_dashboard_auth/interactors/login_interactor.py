from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from covid_dashboard_auth.exceptions.exceptions import InvalidUsername, \
    InvalidPassword
from covid_dashboard_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface


class LoginInteractor:

    def __init__(self, storage: UserStorageInterface,
                 oauth2storage: OAuth2SQLStorage):

        self.storage = storage
        self.oauth2storage = oauth2storage

    def login_wrapper(self, username, password, presenter: PresenterInterface):

        try:
            user_token_dto, is_admin = \
                self.login(username=username, password=password)
        except InvalidUsername:
            presenter.raise_exception_for_invalid_username()
        except InvalidPassword:
            presenter.raise_exception_for_invalid_password()
        else:
            return presenter.get_response_for_login(user_token_dto, is_admin)


    def login(self, username, password):

        self.storage.is_valid_username(username)

        user_details_dto = \
            self.storage.is_valid_password(username=username,
                                           password=password)

        service = \
            OAuthUserAuthTokensService(oauth2_storage=self.oauth2storage)

        user_id = user_details_dto.user_id
        is_admin = user_details_dto.is_admin

        user_token_dto = service.create_user_auth_tokens(user_id=user_id)

        return user_token_dto, is_admin
