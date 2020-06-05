import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors\
    .get_day_wise_district_cumulative_statistics_interactor \
        import DistrictDayWiseCumulativeStatisticsInteractor


def test_district_cumulative_details_interactor_with_valid_details_returns_dto(
    district_day_wise_cumulative_dto, day_wise_district_cumulative_response,
    updated_district_day_wise_cumulative_dto):

    # Arrange
    district_id = 1
    expected_dict = day_wise_district_cumulative_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(DistrictStorageInterface)

    presenter.get_day_wise_district_cumulative_statistics_response\
        .return_value = expected_dict
    storage.get_day_wise_district_cumulative_statistics.return_value = \
        district_day_wise_cumulative_dto

    interactor = DistrictDayWiseCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = \
        interactor.get_day_wise_district_cumulative_statistics(district_id)

    # Assert
    assert response == expected_dict
    storage.get_day_wise_district_cumulative_statistics\
        .assert_called_once_with(district_id=district_id)
    presenter.get_day_wise_district_cumulative_statistics_response\
        .assert_called_once_with(
            day_wise_district_cumulative_dto=updated_district_day_wise_cumulative_dto
        )

def test_district_cumulative_details_interactor_with_invalid_district_id_raises_exception():

    # Arrange
    district_id = -1
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(DistrictStorageInterface)

    presenter.raise_exception_for_invalid_district.side_effect = NotFound
    storage.is_valid_district_id.side_effect = InvalidDistrict

    interactor = DistrictDayWiseCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.get_day_wise_district_cumulative_statistics(district_id)

    # Assert
    storage.is_valid_district_id.assert_called_once_with(district_id=district_id)
    presenter.raise_exception_for_invalid_district.assert_called_once_with()
