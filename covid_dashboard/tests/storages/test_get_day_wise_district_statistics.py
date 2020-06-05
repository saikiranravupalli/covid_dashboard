import pytest
from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation

@pytest.mark.django_db
def test_get_day_wise_district_statistics_returns_state_day_wise_dtos(
    daily_statistics, district_day_wise_statistics_dtos):

    # Arrange
    district_id = 1
    storage = DistrictStorageImplementation()

    # Act
    district_statistics_dtos = \
        storage.get_day_wise_district_statistics(district_id=district_id)

    # Assert
    assert district_statistics_dtos == district_day_wise_statistics_dtos
