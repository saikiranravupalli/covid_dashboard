import pytest

from covid_dashboard.storages.state_storage_implementation import \
    StateStorageImplementation


@pytest.mark.django_db
def test_get_state_cumulative_statistics_returns_state_cumulative_dtos(
    daily_statistics, district_stats_dto, state_stats_dto):

    # Arrange
    till_date = '27/05/2020'
    storage = StateStorageImplementation()
    
    # Act
    state_cumulative_dto = storage.get_state_cumulative_statistics(till_date)

    # Assert
    assert state_cumulative_dto == state_stats_dto
