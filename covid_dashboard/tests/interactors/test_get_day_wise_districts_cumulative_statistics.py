from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.storages.dtos import \
    DistrictsDayWiseCumulativeStatisticsDto
from covid_dashboard.interactors\
    .districts_day_wise_cumulative_statistics_interactor \
        import DistrictsDayWiseCumulativeStatisticsInteractor


def test_district_cumulative_details_interactor_with_valid_details_returns_dto(
    districts_day_wise_stats, districts_day_wise_cumulative_stats,
    day_wise_district_cumulative_response):

    # Arrange
    expected_dict = day_wise_district_cumulative_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(DistrictStorageInterface)

    presenter.get_day_wise_districts_cumulative_statistics_response\
        .return_value = expected_dict
    storage.get_day_wise_districts_cumulative_statistics.return_value = \
        districts_day_wise_stats

    interactor = DistrictsDayWiseCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    response = interactor.get_day_wise_districts_cumulative_statistics()

    # Assert
    assert response == expected_dict
    storage.get_day_wise_districts_cumulative_statistics.assert_called_once()
    presenter.get_day_wise_districts_cumulative_statistics_response\
        .assert_called_once_with(
            day_wise_districts_cumulative_dtos=districts_day_wise_cumulative_stats
        )
