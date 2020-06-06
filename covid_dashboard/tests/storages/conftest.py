import pytest
from datetime import datetime, date
from covid_dashboard.models import User, DailyStatistics, \
    Mandal, District, State
from covid_dashboard.interactors.storages.dtos import \
    UserDetailsDto, DistrictActiveCasesDto, StateCumulativeStatisticsDto, \
    StateDayWiseCumulativeStatisticsDto, DistrictDayWiseStatisticsDto, \
    DistrictsDayWiseCumulativeStatisticsDto, DistrictStatisticsDto, \
    StateStatisticsDto, MandalActiveCasesDto, DistrictCumulativeStatisticsDto,\
    StateDayWiseStatisticsDto, DailyStatisticsDto, MandalStatisticsDto, \
    DistrictDayWiseCumulativeStatisticsDto, DistrictOnDateStatisticsDto, \
    MandalDayWiseStatisticsDto, MandalsDayWiseCumulativeStatisticsDto, \
    DistrictDailyStatisticsDto

@pytest.fixture()
def districts_list():
    districts_list = [
        {
            "name": "district_1",
            "state_id": 1
        },
        {
            "name": "district_2",
            "state_id": 1
        },
        {
            "name": "district_3",
            "state_id": 1
        }
    ]
    return districts_list

@pytest.fixture()
def mandals_list():
    mandals_list = [
        {
            "name": "mandal_1",
            "district_id": 1
        },
        {
            "name": "mandal_2",
            "district_id": 1
        },
        {
            "name": "mandal_3",
            "district_id": 2
        },
        {
            "name": "mandal_4",
            "district_id": 2
        }
    ]
    return mandals_list

@pytest.fixture()
def daily_statistics_list():
    daily_statistics = [
        {
            "for_date":"2020/05/27",
            "total_confirmed": 100,
            "total_deaths": 10,
            "total_recovered": 80,
            "mandal_id": 1
        },
        {
            "for_date":"2020/05/26",
            "total_confirmed": 100,
            "total_deaths": 10,
            "total_recovered": 70,
            "mandal_id": 1
        },
        {
            "for_date":"2020/05/27",
            "total_confirmed": 100,
            "total_deaths": 20,
            "total_recovered": 60,
            "mandal_id": 2
        },
        {
            "for_date":"2020/05/26",
            "total_confirmed": 100,
            "total_deaths": 20,
            "total_recovered": 40,
            "mandal_id": 2
        },
        {
            "for_date":"2020/05/27",
            "total_confirmed": 100,
            "total_deaths": 10,
            "total_recovered": 50,
            "mandal_id": 3
        },
        {
            "for_date":"2020/05/26",
            "total_confirmed": 100,
            "total_deaths": 20,
            "total_recovered": 40,
            "mandal_id": 3
        },
        {
            "for_date":"2020/05/27",
            "total_confirmed": 100,
            "total_deaths": 5,
            "total_recovered": 30,
            "mandal_id": 4
        },
        {
            "for_date":"2020/05/26",
            "total_confirmed": 100,
            "total_deaths": 25,
            "total_recovered": 25,
            "mandal_id": 4
        }
    ]
    return daily_statistics

@pytest.fixture()
def user():
    user = User.objects.create(
        username='user_1'
    )
    user.set_password('password')
    user.save()
    return user

@pytest.fixture()
def superuser():
    user = User.objects.create(
        username='user_1',
        is_admin=True
    )
    user.set_password('password')
    user.save()
    return user

@pytest.fixture()
def user_dto():
    user_dto = UserDetailsDto(
        user_id=1,
        is_admin=False
    )
    return user_dto

@pytest.fixture()
def state():
    state = State.objects.create(name='state_1')
    return state.id

@pytest.fixture()
def districts(state, districts_list):
    district_objs = [
        District(
            name=district['name'],
            state_id=district['state_id']
        )
        for district in districts_list
    ]
    District.objects.bulk_create(district_objs)

@pytest.fixture()
def mandals(districts, mandals_list):
    mandal_objs = [
        Mandal(
            name=mandal['name'],
            district_id=mandal['district_id']
        )
        for mandal in mandals_list
    ]
    Mandal.objects.bulk_create(mandal_objs)

@pytest.fixture()
def daily_statistics(mandals, daily_statistics_list):
    daily_statistics = [
        DailyStatistics(
            for_date=datetime.strptime(daily_stat['for_date'], '%Y/%m/%d').date(),
            total_confirmed=daily_stat['total_confirmed'],
            total_deaths=daily_stat['total_deaths'],
            total_recovered=daily_stat['total_recovered'],
            mandal_id=daily_stat['mandal_id']
        )
        for daily_stat in daily_statistics_list
    ]
    DailyStatistics.objects.bulk_create(daily_statistics)

@pytest.fixture()
def district_stats_dto():
    district_stats_dto = [
        DistrictActiveCasesDto(
            district_id=1,
            name='district_1',
            total_confirmed=400,
            total_deaths=60,
            total_recovered=250,
            total_active=90
        ),
        DistrictActiveCasesDto(
            district_id=2,
            name='district_2',
            total_confirmed=400,
            total_deaths=60,
            total_recovered=145,
            total_active=195
        ),
        DistrictActiveCasesDto(
            district_id=3,
            name='district_3',
            total_confirmed=0,
            total_deaths=0,
            total_recovered=0,
            total_active=0
        )
    ]
    return district_stats_dto

@pytest.fixture()
def state_stats_dto(district_stats_dto):
    state_stats_dto = StateCumulativeStatisticsDto(
        name='state_1',
        total_confirmed=800,
        total_deaths=120,
        total_recovered=395,
        total_active=285,
        districts=district_stats_dto
    )
    return state_stats_dto

@pytest.fixture()
def state_day_wise_dtos():
    state_day_wise_dtos = [
        StateDayWiseCumulativeStatisticsDto(
            name='state_1',
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=400,
            total_deaths=75,
            total_recovered=175,
            total_active=150
        ),
        StateDayWiseCumulativeStatisticsDto(
            name='state_1',
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=400,
            total_deaths=45,
            total_recovered=220,
            total_active=135
        )
    ]
    return state_day_wise_dtos

@pytest.fixture()
def district1_day_wise_dtos():
    district_day_wise_dtos = [
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=110,
            total_active=60
        ),
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=140,
            total_active=30
        ),
    ]
    return district_day_wise_dtos

@pytest.fixture()
def district_day_wise_statistics_dtos():
    district_day_wise_statistics_dtos = [
        DistrictDailyStatisticsDto(
            name='district_1',
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=110
        ),
        DistrictDailyStatisticsDto(
            name='district_1',
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=140
        )
    ]
    return district_day_wise_statistics_dtos

@pytest.fixture()
def district2_day_wise_dtos():
    district_day_wise_dtos = [
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=200,
            total_deaths=45,
            total_recovered=65,
            total_active=90
        ),
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=200,
            total_deaths=15,
            total_recovered=80,
            total_active=105
        )
    ]
    return district_day_wise_dtos

@pytest.fixture()
def district_day_wise_dto(district1_day_wise_dtos):
    district_day_wise_dto = \
        DistrictDayWiseCumulativeStatisticsDto(
            name='district_1',
            date_wise_details=district1_day_wise_dtos
        )
    return district_day_wise_dto

@pytest.fixture()
def districts_day_wise_dtos(district1_day_wise_dtos, district2_day_wise_dtos):
    districts_day_wise_dtos = [
        DistrictsDayWiseCumulativeStatisticsDto(
            district_id=1,
            name='district_1',
            date_wise_details=district1_day_wise_dtos
        ),
        DistrictsDayWiseCumulativeStatisticsDto(
            district_id=2,
            name='district_2',
            date_wise_details=district2_day_wise_dtos
        ),
        DistrictsDayWiseCumulativeStatisticsDto(
            district_id=3,
            name='district_3',
            date_wise_details=[]
        )
    ]
    return districts_day_wise_dtos

@pytest.fixture()
def mandal1_day_wise_dtos():
    mandal1_day_wise_dtos = [
        MandalDayWiseStatisticsDto(
            till_date=date(2020, 5, 26),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=70,
            total_active=20,
        ),
        MandalDayWiseStatisticsDto(
            till_date=date(2020, 5, 27),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=80,
            total_active=10
        )
    ]
    return mandal1_day_wise_dtos

@pytest.fixture()
def mandal2_day_wise_dtos():
    mandal2_day_wise_dtos = [
        MandalDayWiseStatisticsDto(
            till_date=date(2020, 5, 26),
            total_confirmed=100,
            total_deaths=20,
            total_recovered=40,
            total_active=40,
        ),
        MandalDayWiseStatisticsDto(
            till_date=date(2020, 5, 27),
            total_confirmed=100,
            total_deaths=20,
            total_recovered=60,
            total_active=20
        )
    ]
    return mandal2_day_wise_dtos

@pytest.fixture()
def mandals_day_wise_dtos(mandal1_day_wise_dtos, mandal2_day_wise_dtos):
    mandals_day_wise_dtos = [
        MandalsDayWiseCumulativeStatisticsDto(
            mandal_id=1,
            name='mandal_1',
            date_wise_details=mandal1_day_wise_dtos
        ),
        MandalsDayWiseCumulativeStatisticsDto(
            mandal_id=2,
            name='mandal_2',
            date_wise_details=mandal2_day_wise_dtos
        )
    ]
    return mandals_day_wise_dtos
    

@pytest.fixture()
def district_statistics_dtos():
    district_statistics_dtos = [
        DistrictStatisticsDto(
            district_id=1,
            name="district_1",
            total_confirmed=200,
            total_deaths=30,
            total_recovered=110
        ),
        DistrictStatisticsDto(
            district_id=2,
            name="district_2",
            total_confirmed=200,
            total_deaths=45,
            total_recovered=65
        )
    ]
    return district_statistics_dtos

@pytest.fixture()
def mandal_statistics_dtos():
    mandal_statistics_dtos = [
        MandalStatisticsDto(
            mandal_id=1,
            name='mandal_1',
            total_confirmed=100,
            total_deaths=10,
            total_recovered=70
        ),
        MandalStatisticsDto(
            mandal_id=2,
            name='mandal_2',
            total_confirmed=100,
            total_deaths=20,
            total_recovered=40
        ),
        MandalStatisticsDto(
            mandal_id=3,
            name='mandal_3',
            total_confirmed=0,
            total_deaths=0,
            total_recovered=0
        ),
        MandalStatisticsDto(
            mandal_id=4,
            name='mandal_4',
            total_confirmed=0,
            total_deaths=0,
            total_recovered=0
        )
    ]
    mandal_statistics_dtos

@pytest.fixture()
def district_statistics_dto(mandal_statistics_dtos):
    district_statistics_dto = DistrictOnDateStatisticsDto(
        name='district_1',
        total_confirmed=200,
        total_recovered=110,
        total_deaths=30,
        mandals=mandal_statistics_dtos
    )
    return district_statistics_dto

@pytest.fixture()
def state_statistics_dto(district_statistics_dtos):
    state_statistics_dto = StateStatisticsDto(
        name='state_1',
        total_confirmed=400,
        total_deaths=75,
        total_recovered=175,
        districts=district_statistics_dtos
    )
    return state_statistics_dto

@pytest.fixture()
def mandal_cumulative_statistics_dtos():
    mandal_cumulative_statistics_dtos =  [
        MandalActiveCasesDto(
            mandal_id=1,
            name='mandal_1',
            total_confirmed=200,
            total_deaths=20,
            total_recovered=150,
            total_active=30
        ),
        MandalActiveCasesDto(
            mandal_id=2,
            name='mandal_2',
            total_confirmed=200,
            total_deaths=40,
            total_recovered=100,
            total_active=60
        )
    ]
    return mandal_cumulative_statistics_dtos

@pytest.fixture()
def district_cumulative_statistics_dto(mandal_cumulative_statistics_dtos):
    district_cumulative_staticstics_dto = \
        DistrictCumulativeStatisticsDto(
            name='district_1',
            total_confirmed=400,
            total_deaths=60,
            total_recovered=250,
            total_active=90,
            mandals=mandal_cumulative_statistics_dtos
        )
    return district_cumulative_staticstics_dto

@pytest.fixture()
def state_day_wise_statistics_dtos():
    state_day_wise_dtos = [
        StateDayWiseStatisticsDto(
            name='state_1',
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=400,
            total_deaths=75,
            total_recovered=175
        ),
        StateDayWiseStatisticsDto(
            name='state_1',
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=400,
            total_deaths=45,
            total_recovered=220
        )
    ]
    return state_day_wise_dtos

@pytest.fixture()
def daily_statistics_dtos():
    daily_statistics_dtos = [
        DailyStatisticsDto(
            for_date=date(2020, 5, 27),
            district_id=1,
            district_name='district_1',
            mandal_id=1,
            mandal_name='mandal_1',
            total_confirmed=100,
            total_deaths=10,
            total_recovered=80,
        ),
        DailyStatisticsDto(
            for_date=date(2020, 5, 26),
            district_id=1,
            district_name='district_1',
            mandal_id=1,
            mandal_name='mandal_1',
            total_confirmed=100,
            total_deaths=10,
            total_recovered=70,
        ),
        DailyStatisticsDto(
            for_date=date(2020, 5, 27),
            district_id=1,
            district_name='district_1',
            mandal_id=2,
            mandal_name='mandal_2',
            total_confirmed=100,
            total_deaths=20,
            total_recovered=60,
        ),
        DailyStatisticsDto(
            for_date=date(2020, 5, 26),
            district_id=1,
            district_name='district_1',
            mandal_id=2,
            mandal_name='mandal_2',
            total_confirmed=100,
            total_deaths=20,
            total_recovered=40,
        ),
        DailyStatisticsDto(
            for_date=date(2020, 5, 27),
            district_id=2,
            district_name='district_2',
            mandal_id=3,
            mandal_name='mandal_3',
            total_confirmed=100,
            total_deaths=10,
            total_recovered=50,
        ),
        DailyStatisticsDto(
            for_date=date(2020, 5, 26),
            district_id=2,
            district_name='district_2',
            mandal_id=3,
            mandal_name='mandal_3',
            total_confirmed=100,
            total_deaths=20,
            total_recovered=40,
        ),
        DailyStatisticsDto(
            for_date=date(2020, 5, 27),
            district_id=2,
            district_name='district_2',
            mandal_id=4,
            mandal_name='mandal_4',
            total_confirmed=100,
            total_deaths=5,
            total_recovered=30,
        ),
        DailyStatisticsDto(
            for_date=date(2020, 5, 27),
            district_id=2,
            district_name='district_2',
            mandal_id=4,
            mandal_name='mandal_4',
            total_confirmed=100,
            total_deaths=25,
            total_recovered=25,
        )
    ]
    return daily_statistics_dtos
