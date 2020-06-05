import pytest

from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation


@pytest.mark.django_db
def test_get_daily_statistics_returns_daily_statistics_dtos(
    daily_statistics, daily_statistics_dtos):

    # Arrange
    storage = MandalStorageImplementation()
    
    # Act
    daily_statistics_dtos = storage.get_daily_statistics()

    # Assert
    assert daily_statistics_dtos == daily_statistics_dtos
