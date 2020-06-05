import pytest

from covid_dashboard.models import DailyStatistics
from covid_dashboard.exceptions.exceptions import InvalidMandalStatistics
from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation

@pytest.mark.django_db
def test_is_valid_mandal_stats_given_invalid_details_raises_exception():

    # Arrange
    mandal_id = 1
    for_date = '2020/05/10'
    storage = MandalStorageImplementation()

    # Act
    with pytest.raises(InvalidMandalStatistics):
        storage.is_mandal_stats_exists(
            for_date=for_date,
            mandal_id=mandal_id
        )
