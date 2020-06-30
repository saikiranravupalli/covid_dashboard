import factory
from datetime import date, timedelta
from faker import Faker

from covid_dashboard.models import District, Mandal, \
    State, DailyStatistics
from factory.fuzzy import FuzzyInteger

def date_range(start_date=None, end_date=None):
    span = end_date - start_date
    for i in range(span.days + 1):
        yield start_date + timedelta(days=i)

DATES_RANGE = [
    date
    for date in date_range(
        start_date=date(2020, 6, 1),
        end_date=date(2020, 6, 5)
    )
]
TOTAL_DEATHS = [10, 20, 30, 40, 50, 100]
TOTAL_CONFIRMED = [300, 400, 500, 600, 700, 800]
TOTAL_RECOVERED = [60, 70, 80, 90, 100, 150]


class StateFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = State

    name = factory.Sequence(lambda n: f'state{n}')

class DistrictFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = District

    name = factory.Sequence(lambda n: f'district{n}')
    state = factory.SubFactory(StateFactory)

class MandalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Mandal

    name = factory.Sequence(lambda n: f'mandal{n}')
    district = factory.SubFactory(DistrictFactory)

class DailyStatisticsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DailyStatistics

    for_date = factory.Iterator(DATES_RANGE)
    total_confirmed = factory.Iterator(TOTAL_CONFIRMED)
    total_deaths = factory.Iterator(TOTAL_DEATHS)
    total_recovered = factory.Iterator(TOTAL_RECOVERED)
    mandal = factory.SubFactory(MandalFactory)
