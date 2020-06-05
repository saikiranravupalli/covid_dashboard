from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from covid_dashboard.exceptions.exceptions import InvalidUsername, \
    InvalidPassword
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.storages.user_storage_interface import \
    UserStorageInterface


class LoginInteractor:
    def __init__(self, storage: UserStorageInterface,
                 oauth2storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.storage = storage
        self.oauth2storage = oauth2storage
        self.presenter = presenter

    def login(self, username, password):
        try:
            self.storage.is_valid_username(username)
        except InvalidUsername:
            self.presenter.raise_exception_for_invalid_username()

        try:
            user_details_dto = self.storage.is_valid_password(
                username=username,
                password=password
            )
        except InvalidPassword:
            self.presenter.raise_exception_for_invalid_password()
            return

        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2storage
        )

        user_id = user_details_dto.user_id
        is_admin = user_details_dto.is_admin

        tokens_dto = service.create_user_auth_tokens(user_id=user_id)

        return self.presenter.get_response_for_login(tokens_dto, is_admin)
