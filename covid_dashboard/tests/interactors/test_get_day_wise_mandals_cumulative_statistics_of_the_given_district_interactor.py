import pytest
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
    DistrictsDayWiseCumulativeStatisticsDto
from covid_dashboard.interactors\
    .get_day_wise_mandal_cumulative_stats_of_the_given_district_interactor \
        import MandalsDayWiseCumulativeStatisticsInteractor

def test_mandals_cumulative_details_interactor_with_invalid_district_raises_exception():

    # Arrange
    district_id = 1
    presenter = create_autospec(PresenterInterface)
    mandal_storage = create_autospec(MandalStorageInterface)
    district_storage = create_autospec(DistrictStorageInterface)

    district_storage.is_valid_district_id.side_effect = InvalidDistrict
    presenter.raise_exception_for_invalid_district.side_effect = BadRequest

    interactor = MandalsDayWiseCumulativeStatisticsInteractor(
        district_storage=district_storage,
        mandal_storage=mandal_storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(BadRequest):
        interactor\
            .get_day_wise_mandals_cumulative_statistics_of_the_given_district(
                district_id=district_id)

    # Assert
    district_storage.is_valid_district_id.assert_called_once_with(
        district_id=district_id)
    presenter.raise_exception_for_invalid_district.assert_called_once()

def test_mandals_cumulative_details_interactor_with_valid_details_returns_dto(
    mandals_day_wise_cumulative_stats, mandals_day_wise_stats,
    day_wise_mandals_cumulative_response):

    # Arrange
    district_id = 1
    expected_dict = day_wise_mandals_cumulative_response
    presenter = create_autospec(PresenterInterface)
    mandal_storage = create_autospec(MandalStorageInterface)
    district_storage = create_autospec(DistrictStorageInterface)

    presenter.get_day_wise_mandals_cumulative_statistics_response\
        .return_value = expected_dict
    mandal_storage.get_day_wise_mandals_cumulative_statistics.return_value = \
        mandals_day_wise_stats

    interactor = MandalsDayWiseCumulativeStatisticsInteractor(
        district_storage=district_storage,
        mandal_storage=mandal_storage,
        presenter=presenter
    )

    # Act
    response = interactor\
        .get_day_wise_mandals_cumulative_statistics_of_the_given_district(
            district_id=district_id)

    # Assert
    assert response == expected_dict
    mandal_storage.get_day_wise_mandals_cumulative_statistics.assert_called_once_with(
        district_id=district_id)
    presenter.get_day_wise_mandals_cumulative_statistics_response\
        .assert_called_once_with(
            day_wise_mandals_cumulative_dtos=mandals_day_wise_cumulative_stats
        )
