import pytest
from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation

@pytest.mark.django_db
def test_get_day_wise_mandals_cumulative_statistics_returns_day_wise_(
    daily_statistics, mandals_day_wise_dtos):

    # Arrange
    district_id = 1
    storage = MandalStorageImplementation()

    # Act
    mandals_day_wise_cumulative_dtos = \
        storage.get_day_wise_mandals_cumulative_statistics(
            district_id=district_id)

    # Assert
    assert mandals_day_wise_cumulative_dtos == mandals_day_wise_dtos
