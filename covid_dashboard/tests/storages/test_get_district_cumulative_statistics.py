import pytest

from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation


@pytest.mark.django_db
def test_get_district_cumulative_statistics_returns_district_cumulative_dtos(
    daily_statistics, district_cumulative_statistics_dto):

    # Arrange
    till_date = '27/05/2020'
    district_id = 1
    storage = DistrictStorageImplementation()
    
    # Act
    district_cumulative_dto = \
        storage.get_district_cumulative_statistics(
            till_date=till_date,
            district_id=district_id
        )

    # Assert
    assert district_cumulative_dto == district_cumulative_statistics_dto
