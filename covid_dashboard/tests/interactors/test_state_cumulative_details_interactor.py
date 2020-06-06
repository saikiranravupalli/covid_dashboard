import pytest
from datetime import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface
from covid_dashboard.interactors.storages.dtos import \
    StateCumulativeStatisticsDto
from covid_dashboard.interactors.state_cumulative_statistics_interactor \
    import StateCumulativeStatisticsInteractor


def test_state_cumulative_details_interactor_with_valid_details_returns_dto(
    state_cumulative_dto, state_cumulative_response):

    # Arrange
    till_date = "2020/05/27"
    expected_dict = state_cumulative_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StateStorageInterface)

    presenter.get_state_cumulative_statistics_response.return_value = \
        expected_dict
    storage.get_state_cumulative_statistics.return_value = \
        state_cumulative_dto

    interactor = StateCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_state_cumulative_statistics(
        till_date=till_date
    )

    # Assert
    assert response == expected_dict
    storage.get_state_cumulative_statistics.assert_called_once_with(
        till_date=till_date
    )
    presenter.get_state_cumulative_statistics_response\
        .assert_called_once_with(
            state_cumulative_statistics_dto=state_cumulative_dto
        )

def test_state_cumulative_details_interactor_with_invalid_details_returns_empty_list():

    # Arrange
    till_date = "2020/02/27"
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StateStorageInterface)
    storage.get_state_cumulative_statistics.return_value = None
    expected_dict = {
        "name": "AndhraPradesh",
        "total_confirmed": 0,
        "total_active": 0,
        "total_deaths": 0,
        "total_recovered": 0,
        "districts": []
    }

    interactor = StateCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_state_cumulative_statistics(
        till_date=till_date
    )

    # Assert
    assert response == expected_dict
    storage.get_state_cumulative_statistics.assert_called_once_with(
        till_date=till_date
    )
