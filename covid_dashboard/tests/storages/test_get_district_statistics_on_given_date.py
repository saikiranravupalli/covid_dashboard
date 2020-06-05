import pytest

from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation


@pytest.mark.django_db
def test_get_district_statistics_on_given_date_returns_district_statistics_dto(
    daily_statistics, district_statistics_dto):

    # Arrange
    for_date = '2020/05/26'
    district_id = 1
    storage = MandalStorageImplementation()
    
    # Act
    district_statistics_dto = \
        storage.get_district_statistics_on_given_date(for_date, district_id)

    # Assert
    assert district_statistics_dto == district_statistics_dto
