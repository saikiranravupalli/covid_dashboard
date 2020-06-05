import pytest
from datetime import datetime
from django_swagger_utils.drf_server.exceptions import BadRequest
from mock import create_autospec

from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.storages.dtos import \
    StateStatisticsDto
from covid_dashboard.interactors\
    .get_day_wise_district_details_on_given_date_interactor \
        import DistrictStatisticsInteractor


def test_get_district_stats_on_given_date_interactor_with_valid_details_returns_dto(
    district_statistics_dto, district_statistics_response):

    # Arrange
    for_date = "2020/05/27"
    district_id = 1
    expected_dict = district_statistics_response
    presenter = create_autospec(PresenterInterface)
    district_storage = create_autospec(DistrictStorageInterface)
    mandal_storage = create_autospec(MandalStorageInterface)

    presenter.get_district_statistics_on_given_date_response.return_value = \
        expected_dict
    mandal_storage.get_district_statistics_on_given_date.return_value = \
        district_statistics_dto

    interactor = DistrictStatisticsInteractor(
        district_storage=district_storage,
        mandal_storage=mandal_storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_district_statistics_on_given_date(
        district_id=district_id,
        for_date=for_date
    )

    # Assert
    assert response == expected_dict
    mandal_storage.get_district_statistics_on_given_date\
        .assert_called_once_with(
            for_date=for_date,
            district_id=district_id
        )
    presenter.get_district_statistics_on_given_date_response\
        .assert_called_once_with(
            district_statistics_on_date_dto=district_statistics_dto
        )

def test_get_district_stats_on_given_date_with_no_data_on_that_date_returns_empty_list():

    # Arrange
    for_date = "2020/02/27"
    district_id = 1
    presenter = create_autospec(PresenterInterface)
    district_storage = create_autospec(DistrictStorageInterface)
    mandal_storage = create_autospec(MandalStorageInterface)
    mandal_storage.get_district_statistics_on_given_date.return_value = \
        None

    interactor = DistrictStatisticsInteractor(
        district_storage=district_storage,
        mandal_storage=mandal_storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_district_statistics_on_given_date(
        district_id=district_id,
        for_date=for_date
    )

    # Assert
    assert response == []
    mandal_storage.get_district_statistics_on_given_date\
        .assert_called_once_with(
            for_date=for_date,
            district_id=district_id
        )

def test_get_district_stats_on_given_date_with_invlalid_district_id_raises_exception():

    # Arrange
    district_id = -1
    for_date = "2020/02/27"
    presenter = create_autospec(PresenterInterface)
    district_storage = create_autospec(DistrictStorageInterface)
    mandal_storage = create_autospec(MandalStorageInterface)

    presenter.raise_exception_for_invalid_district.side_effect = BadRequest
    district_storage.is_valid_district_id.side_effect = InvalidDistrict

    interactor = DistrictStatisticsInteractor(
        district_storage=district_storage,
        mandal_storage=mandal_storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(BadRequest):
        interactor.get_district_statistics_on_given_date(
            district_id=district_id,
            for_date=for_date
        )

    # Assert
    district_storage.is_valid_district_id.assert_called_once_with(
        district_id=district_id)
    presenter.raise_exception_for_invalid_district.assert_called_once_with()

