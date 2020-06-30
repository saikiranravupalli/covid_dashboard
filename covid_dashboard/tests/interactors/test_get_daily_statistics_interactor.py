import pytest
from django_swagger_utils.drf_server.exceptions import Forbidden
from mock import create_autospec, patch

from covid_dashboard.exceptions.exceptions import InvalidAccess
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.get_daily_statistics_interactor import \
    DailyStatisticsInteractor
from covid_dashboard_auth.interactors.storages.dtos import UserDetailsDTO


@patch('covid_dashboard_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_given_invalid_admin_raises_exception(get_user_dto):

    # Arrange
    invalid_user_admin = 1
    storage = create_autospec(MandalStorageInterface)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_exception_for_invalid_user_admin.side_effect = \
        Forbidden
    get_user_dto.return_value = UserDetailsDTO(
        user_id=1,
        is_admin=False
    )
    interactor = DailyStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(Forbidden):
        interactor.get_daily_statistics(user_id=invalid_user_admin)

    # Assert
    presenter.raise_exception_for_invalid_user_admin.assert_called_once()

@patch('covid_dashboard_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_daily_statistics_with_valid_user_details_returns_statistics_dict(
    get_user_dto, get_daily_statistics_response, get_daily_statistics_dtos):

    # Arrange
    user_id = 1
    expected_dict = get_daily_statistics_response
    storage = create_autospec(MandalStorageInterface)
    presenter = create_autospec(PresenterInterface)
    get_user_dto.return_value = UserDetailsDTO(
        user_id=1,
        is_admin=False
    )
    storage.get_daily_statistics.return_value = get_daily_statistics_dtos
    presenter.get_daily_statistics_response.return_value = \
        get_daily_statistics_response
    interactor = DailyStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_daily_statistics(user_id=user_id)

    # Assert
    assert expected_dict == response
    storage.get_daily_statistics.assert_called_once()
    presenter.get_daily_statistics_response.assert_called_once_with(
        daily_statistics_dtos=get_daily_statistics_dtos
    )
