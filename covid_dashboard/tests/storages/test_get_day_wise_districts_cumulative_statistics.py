import pytest
from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation

@pytest.mark.django_db
def test_get_day_wise_districts_cumulative_statistics_returns_day_wise_(
    daily_statistics, districts_day_wise_dtos):

    # Arrange
    storage = DistrictStorageImplementation()

    # Act
    districts_day_wise_cumulative_dto = \
        storage.get_day_wise_districts_cumulative_statistics()

    # Assert
    assert districts_day_wise_cumulative_dto == districts_day_wise_dtos
