import pytest
from datetime import datetime

from covid_dashboard.models import DailyStatistics
from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation

@pytest.mark.django_db
def test_update_mandal_statistics_with_valid_details_updates_mandals_statistics(
    daily_statistics
):
    for_date="2020/05/27"
    total_confirmed=30
    total_deaths=5
    total_recovered=20
    mandal_id=1
    storage = MandalStorageImplementation()

    storage.update_mandal_statistics(
        for_date=for_date,
        total_confirmed=total_confirmed,
        total_deaths=total_deaths,
        total_recovered=total_recovered,
        mandal_id=mandal_id
    )
    for_date = datetime.strptime(for_date, '%Y/%m/%d').date()

    # Act
    daily_stats = DailyStatistics.objects.get(
        mandal_id=mandal_id,
        for_date=for_date
    )

    # Assert
    assert daily_stats.total_confirmed == total_confirmed
    assert daily_stats.total_deaths == total_deaths
    assert daily_stats.total_recovered == total_recovered
