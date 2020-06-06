import pytest
from datetime import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface
from covid_dashboard.interactors.storages.dtos import \
    StateStatisticsDto
from covid_dashboard.interactors.get_state_stats_on_given_date_interactor \
    import StateStatisticsInteractor


def test_get_state_stats_on_given_date_interactor_with_valid_details_returns_dto(
    state_statistics_dto, state_statistics_response):

    # Arrange
    for_date = "2020/05/27"
    expected_dict = state_statistics_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StateStorageInterface)

    presenter.get_state_statistics_on_given_date_response.return_value = \
        expected_dict
    storage.get_state_statistics_on_given_date.return_value = \
        state_statistics_dto

    interactor = StateStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_state_statistics_on_given_date(
        for_date=for_date
    )

    # Assert
    assert response == expected_dict
    storage.get_state_statistics_on_given_date.assert_called_once_with(
        for_date=for_date
    )
    presenter.get_state_statistics_on_given_date_response\
        .assert_called_once_with(
            state_statistics_dto=state_statistics_dto
        )

def test_state_cumulative_details_interactor_with_invalid_details_returns_dict_with_zeroes():

    # Arrange
    for_date = "2020/02/27"
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StateStorageInterface)
    storage.get_state_statistics_on_given_date.return_value = None
    expected_dict = {
        "name": "AndhraPradesh",
        "total_confirmed": 0,
        "total_active": 0,
        "total_deaths": 0,
        "total_recovered": 0,
        "districts": []
    }

    interactor = StateStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_state_statistics_on_given_date(
        for_date=for_date
    )

    # Assert
    assert response == expected_dict
    storage.get_state_statistics_on_given_date.assert_called_once_with(
        for_date=for_date
    )
