import pytest
from datetime import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface
from covid_dashboard.interactors.storages.dtos import \
    StateDayWiseCumulativeStatisticsDto
from covid_dashboard.interactors\
    .state_day_wise_cumulative_statistics_interactor \
        import StateDayWiseCumulativeStatisticsInteractor


def test_state_cumulative_details_interactor_with_valid_details_returns_dto(
    state_day_wise_cumulative_dto, day_wise_state_cumulative_response,
    updated_state_day_wise_cumulative_dto):

    # Arrange
    expected_dict = day_wise_state_cumulative_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StateStorageInterface)

    presenter.get_day_wise_state_cumulative_statistics_response\
        .return_value = expected_dict
    storage.get_day_wise_state_cumulative_statistics.return_value = \
        state_day_wise_cumulative_dto

    interactor = StateDayWiseCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_day_wise_state_cumulative_statistics()

    # Assert
    assert response == expected_dict
    storage.get_day_wise_state_cumulative_statistics.assert_called_once()
    presenter.get_day_wise_state_cumulative_statistics_response\
        .assert_called_once_with(
            day_wise_state_cumulative_dtos=updated_state_day_wise_cumulative_dto
        )
