import pytest
from covid_dashboard.storages.state_storage_implementation import \
    StateStorageImplementation

@pytest.mark.django_db
def test_get_day_wise_state_cumulative_statistics_returns_state_day_wise_dtos(
    daily_statistics, state_day_wise_dtos):

    # Arrange
    storage = StateStorageImplementation()

    # Act
    state_day_wise_cumulative_dto = \
        storage.get_day_wise_state_cumulative_statistics()

    # Assert
    assert state_day_wise_cumulative_dto == state_day_wise_dtos
