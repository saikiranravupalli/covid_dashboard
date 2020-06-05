import pytest
import datetime
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import BadRequest
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from covid_dashboard.interactors.storages.dtos import UserDetailsDto
from covid_dashboard.exceptions.exceptions import InvalidUsername, \
    InvalidPassword
from covid_dashboard.interactors.login_interactor import \
    LoginInteractor
from covid_dashboard.interactors.storages.user_storage_interface import \
    UserStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class TestLoginInteractor:
    def test_login_interactor_with_invalid_username_raises_error(self):

        # Arrange
        username = 'invalidusername'
        password = 'invalid'
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.is_valid_username.side_effect = InvalidUsername
        presenter.raise_exception_for_invalid_username.side_effect = BadRequest

        interactor = LoginInteractor(
            storage=storage,
            oauth2storage=oauth2_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(BadRequest):
            interactor.login(
                username=username,
                password=password
            )

        # Assert
        storage.is_valid_username.assert_called_once_with(username=username)
        presenter.raise_exception_for_invalid_username.assert_called_once()

    def test_login_interactor_with_invalid_password_raises_error(self):
        # Arrange
        username = 'user_1'
        password = 'invalidpassword'
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.is_valid_password.side_effect = InvalidPassword
        presenter.raise_exception_for_invalid_password.side_effect = BadRequest

        interactor = LoginInteractor(
            storage=storage,
            oauth2storage=oauth2_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(BadRequest):
            interactor.login(
                username=username,
                password=password
            )

        # Assert
        storage.is_valid_username.assert_called_once_with(username=username)
        storage.is_valid_password.assert_called_once_with(
            username=username,
            password=password
        )
        presenter.raise_exception_for_invalid_password.assert_called_once()

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens',
        return_value=UserAuthTokensDTO(
            user_id=1,
            access_token="123456",
            refresh_token="654321",
            expires_in=datetime.datetime
        )
    )
    def test_login_interactor_with_valid_details_returns_user_details_dict(
        self, user_dto):

        # Arrange
        username = 'user_1'
        password = 'password'
        mock_presenter_response = {
            "access_token": "123456",
            "refresh_token": "654321",
            "is_admin": False
        }
        user_dto = UserDetailsDto(
            user_id=1,
            is_admin=False
        )
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.is_valid_password.return_value = user_dto
        presenter.get_response_for_login.return_value = \
            mock_presenter_response
        
        interactor = LoginInteractor(
            storage=storage,
            oauth2storage=oauth2_storage,
            presenter=presenter
        )

        # Act
        response = interactor.login(
            username=username,
            password=password
        )

        # Assert
        assert response == mock_presenter_response
