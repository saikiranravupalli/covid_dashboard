import datetime
from common.dtos import UserAuthTokensDTO
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_login_with_valid_details_returns_user_token_dict():

    # Arrange
    presenter = PresenterImplementation()
    tokens_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="123456",
        refresh_token="654321",
        expires_in=datetime.datetime
    )
    is_admin = False
    expected_dict = {
        "access_token": "123456",
        "refresh_token": "654321",
        "is_admin": False
    }

    # Act
    response = presenter.get_response_for_login(
        tokens_dto=tokens_dto,
        is_admin=is_admin
    )

    # Assert
    assert response == expected_dict
