import pytest

from covid_dashboard.storages.state_storage_implementation import \
    StateStorageImplementation


@pytest.mark.django_db
def test_get_state_statistics_returns_state_cumulative_dtos(
    daily_statistics, district_statistics_dtos, state_statistics_dto):

    # Arrange
    for_date = '2020/05/27'
    storage = StateStorageImplementation()
    
    # Act
    state_statistics_dto = storage.get_state_statistics_on_given_date(for_date)

    # Assert
    assert state_statistics_dto == state_statistics_dto
