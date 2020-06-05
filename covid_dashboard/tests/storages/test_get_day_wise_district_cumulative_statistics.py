import pytest
from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation

@pytest.mark.django_db
def test_get_day_wise_district_cumulative_statistics_returns_day_wise_(
    daily_statistics, district_day_wise_dto):

    # Arrange
    district_id = 1
    storage = DistrictStorageImplementation()

    # Act
    district_day_wise_cumulative_dto = \
        storage.get_day_wise_district_cumulative_statistics(district_id)

    # Assert
    assert district_day_wise_cumulative_dto == district_day_wise_dto
