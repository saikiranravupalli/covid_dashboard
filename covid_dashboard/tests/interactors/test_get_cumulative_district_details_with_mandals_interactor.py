import pytest
from datetime import datetime
from django_swagger_utils.drf_server.exceptions import BadRequest
from mock import create_autospec

from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.storages.dtos import \
    StateCumulativeStatisticsDto
from covid_dashboard.interactors\
    .get_cumulative_district_details_with_mandals_interactor \
        import DistrictCumulativeStatisticsInteractor

def test_district_cumulative_details_with_invalid_district_id_raises_exceptions():

    # Arrange
    invalid_district_id = -1
    till_date = "2020/05/27"
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(DistrictStorageInterface)
    storage.is_valid_district_id.side_effect = InvalidDistrict
    presenter.raise_exception_for_invalid_district.return_value =  BadRequest
    interactor = DistrictCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    interactor.get_district_cumulative_statistics(
        till_date=till_date,
        district_id=invalid_district_id
    )

    # Assert
    storage.is_valid_district_id.assert_called_once_with(
        district_id=invalid_district_id
    )
    presenter.raise_exception_for_invalid_district.assert_called_once()


def test_district_cumulative_details_interactor_with_valid_details_returns_dto(
    district_cumulative_statistics_dto,
    district_cumulative_statistics_response):

    # Arrange
    till_date = "2020/05/27"
    district_id = 1
    expected_dict = district_cumulative_statistics_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(DistrictStorageInterface)

    presenter.get_district_cumulative_statistics_response.return_value = \
        expected_dict
    storage.get_district_cumulative_statistics.return_value = \
        district_cumulative_statistics_dto

    interactor = DistrictCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_district_cumulative_statistics(
        till_date=till_date,
        district_id=district_id
    )

    # Assert
    assert response == expected_dict
    storage.get_district_cumulative_statistics.assert_called_once_with(
        till_date=till_date, district_id=district_id
    )
    presenter.get_district_cumulative_statistics_response\
             .assert_called_once_with(
                 district_cumulative_statistics_dto=
                 district_cumulative_statistics_dto
            )

def test_district_cumulative_details_interactor_with_invalid_details_returns_empty_list():

    # Arrange
    till_date = "2020/02/27"
    district_id = 1
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(DistrictStorageInterface)
    storage.get_district_cumulative_statistics.return_value = None

    interactor = DistrictCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_district_cumulative_statistics(
        till_date=till_date, district_id=district_id
    )

    # Assert
    assert response == []
    storage.get_district_cumulative_statistics.assert_called_once_with(
        till_date=till_date, district_id=district_id
    )
