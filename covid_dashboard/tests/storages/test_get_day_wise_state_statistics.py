import pytest
from covid_dashboard.storages.state_storage_implementation import \
    StateStorageImplementation

@pytest.mark.django_db
def test_get_day_wise_state_statistics_returns_state_day_wise_dtos(
    daily_statistics, state_day_wise_statistics_dtos):

    # Arrange
    storage = StateStorageImplementation()

    # Act
    state_day_wise_statistics_dtos = \
        storage.get_day_wise_state_statistics()

    # Assert
    assert state_day_wise_statistics_dtos == state_day_wise_statistics_dtos
