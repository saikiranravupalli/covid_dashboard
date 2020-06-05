import pytest
from datetime import datetime
from django_swagger_utils.drf_server.exceptions import BadRequest
from mock import create_autospec

from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.storages.dtos import \
    StateDayWiseStatisticsDto
from covid_dashboard.interactors.get_district_day_wise_details_interactor \
    import DistrictDayWiseStatisticsInteractor


def test_district_day_wise_details_interactor_with_valid_details_returns_dto(
    district_day_wise_details_dtos, district_daily_statistics_response):

    # Arrange
    district_id = 1
    expected_dict = district_daily_statistics_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(DistrictStorageInterface)

    presenter.get_day_wise_district_statistics_response.return_value = \
        expected_dict
    storage.get_day_wise_district_statistics.return_value = \
        district_day_wise_details_dtos

    interactor = DistrictDayWiseStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_day_wise_district_statistics(
        district_id=district_id)

    # Assert
    assert response == expected_dict
    storage.get_day_wise_district_statistics.assert_called_once_with(
        district_id=district_id)
    presenter.get_day_wise_district_statistics_response.assert_called_once_with(
            day_wise_district_statistics_dtos=district_day_wise_details_dtos
    )
