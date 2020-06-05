import pytest
from datetime import datetime

from covid_dashboard.interactors.storages.dtos import \
    DistrictActiveCasesDto, StateCumulativeStatisticsDto, \
    StateDayWiseCumulativeStatisticsDto, DistrictDayWiseStatisticsDto, \
    DistrictsDayWiseCumulativeStatisticsDto, DistrictStatisticsDto, \
    StateStatisticsDto, MandalActiveCasesDto, StateDayWiseStatisticsDto, \
    DistrictCumulativeStatisticsDto, DailyStatisticsDto, \
    DistrictDayWiseCumulativeStatisticsDto, DistrictOnDateStatisticsDto, \
    MandalStatisticsDto, MandalsDayWiseCumulativeStatisticsDto, \
    MandalDayWiseStatisticsDto, DistrictDailyStatisticsDto

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
def state_day_wise_cumulative_dto():
    state_day_wise_cumulative_dto = [
        StateDayWiseCumulativeStatisticsDto(
            name="state_1",
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            total_active=110,
        ),
        StateDayWiseCumulativeStatisticsDto(
            name="state_1",
            till_date=datetime(2020, 5, 28).date(),
            total_confirmed=440,
            total_deaths=60,
            total_recovered=160,
            total_active=220,
        ),
        StateDayWiseCumulativeStatisticsDto(
            name="state_1",
            till_date=datetime(2020, 5, 29).date(),
            total_confirmed=660,
            total_deaths=90,
            total_recovered=240,
            total_active=330,
        )
    ]
    return state_day_wise_cumulative_dto

@pytest.fixture()
def state_day_wise_statistics_dtos():
    state_day_wise_statistics_dtos = [
        StateDayWiseStatisticsDto(
            name="state_1",
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80
        ),
        StateDayWiseStatisticsDto(
            name="state_1",
            till_date=datetime(2020, 5, 28).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80
        ),
        StateDayWiseStatisticsDto(
            name="state_1",
            till_date=datetime(2020, 5, 29).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80
        )
    ]
    return state_day_wise_statistics_dtos

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
        )
    ]
    return districts_day_wise_dtos

@pytest.fixture()
def district_day_wise_dto(district1_day_wise_dtos):
    districts_day_wise_dto = \
        DistrictDayWiseCumulativeStatisticsDto(
            name='district_1',
            date_wise_details=district1_day_wise_dtos
        )

    return districts_day_wise_dto

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
def get_daily_statistics_dtos():
    daily_statistics_dtos = [
        DailyStatisticsDto(
            for_date = datetime(2020, 5, 27),
            district_id=1,
            district_name = 'district_1',
            mandal_id=1,
            mandal_name = 'mandal_1',
            total_confirmed = 20,
            total_deaths = 2,
            total_recovered = 10
        )
    ]
    return daily_statistics_dtos

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
        )
    ]
    return mandal_statistics_dtos

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
def mandal1_day_wise_cumulative_stats():
    mandal_day_wise_cumulative_stats = [
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=100,
            total_active=70
        )
    ]
    return mandal_day_wise_cumulative_stats

@pytest.fixture()
def mandal2_day_wise_cumulative_stats():
    mandal_day_wise_cumulative_stats = [
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=100,
            total_active=70
        )
    ]
    return mandal_day_wise_cumulative_stats

@pytest.fixture()
def mandals_day_wise_cumulative_stats(mandal1_day_wise_cumulative_stats,
                                      mandal2_day_wise_cumulative_stats):

    mandals_day_wise_cumulative_stats = [
        MandalsDayWiseCumulativeStatisticsDto(
            mandal_id=1,
            name='mandal_1',
            date_wise_details = mandal1_day_wise_cumulative_stats
        ),
        MandalsDayWiseCumulativeStatisticsDto(
            mandal_id=2,
            name='mandal_2',
            date_wise_details = mandal2_day_wise_cumulative_stats
        )
    ]

    return mandals_day_wise_cumulative_stats

@pytest.fixture()
def district_day_wise_statistics_dtos():
    district_day_wise_dtos = [
        DistrictDailyStatisticsDto(
            name='district_1',
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=400,
            total_deaths=75,
            total_recovered=175
        ),
        DistrictDailyStatisticsDto(
            name='district_1',
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=400,
            total_deaths=45,
            total_recovered=220
        )
    ]
    return district_day_wise_dtos

@pytest.fixture()
def district_day_wise_statistics_response():
    district_day_wise_statistics_dict = {
        "name": "district_1",
        "day_wise_details": [
            {
                "till_date": "2020/05/26",
                "total_confirmed": 400,
                "total_deaths": 75,
                "total_recovered": 175
            },
            {
                "till_date": "2020/05/27",
                "total_confirmed": 400,
                "total_deaths": 45,
                "total_recovered": 220
            }
        ]
    }
    return district_day_wise_statistics_dict

@pytest.fixture()
def district_statistics_response():
    district_statistics_response = {
        "name": "district_1",
        "total_confirmed": 200,
        "total_deaths": 30,
        "total_recovered": 110,
        "mandals": [
            {
                "mandal_id": 1,
                "name": "mandal_1",
                "total_confirmed": 100,
                "total_deaths": 10,
                "total_recovered": 70
            },
            {
                "mandal_id": 2,
                "name": "mandal_2",
                "total_confirmed": 100,
                "total_deaths": 20,
                "total_recovered": 40
            }
        ]
    }

    return district_statistics_response

@pytest.fixture()
def state_cumulative_response():
    state_cumulative_response = {
        "name": "state_1",
        "total_confirmed": 800,
        "total_deaths": 120,
        "total_recovered": 395,
        "total_active": 285,
        "districts": [
            {
                "district_id": 1,
                "name": "district_1",
                "total_confirmed": 400,
                "total_deaths": 60,
                "total_recovered": 250,
                "total_active": 90
            },
            {
                "district_id": 2,
                "name": "district_2",
                "total_confirmed": 400,
                "total_deaths": 60,
                "total_recovered": 145,
                "total_active": 195
            }
        ]
    }

    return state_cumulative_response

@pytest.fixture()
def day_wise_state_cumulative_response():
    state_cumulative_response = {
        "name": "state_1",
        "date_wise_details": [
            {
                "till_date": "2020/05/27",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80,
                "total_active": 110,
            },
            {
                "till_date": "2020/05/28",
                "total_confirmed": 440,
                "total_deaths": 60,
                "total_recovered": 160,
                "total_active": 220,
            },
            {
                "till_date": "2020/05/29",
                "total_confirmed": 660,
                "total_deaths": 90,
                "total_recovered": 240,
                "total_active": 330,
            }
        ]
    }

    return state_cumulative_response

@pytest.fixture()
def district_cumulative_response():
    district_cumulative_response = {
        "name": "district_1",
        "date_wise_details": [
            {
                "till_date": "2020/05/26",
                "total_confirmed": 200,
                "total_deaths": 30,
                "total_recovered": 110,
                "total_active": 60
            },
            {
                "till_date": "2020/05/27",
                "total_confirmed": 200,
                "total_deaths": 30,
                "total_recovered": 140,
                "total_active": 30
            }
        ]
    }

    return district_cumulative_response

@pytest.fixture()
def day_wise_state_statistics_response():
    state_statistics_response = {
        "name": "state_1",
        "date_wise_details": [
            {
                "till_date": "2020/05/27",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80
            },
            {
                "till_date": "2020/05/28",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80
            },
            {
                "till_date": "2020/05/29",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80
            }
        ]
    }

    return state_statistics_response

@pytest.fixture()
def day_wise_district_cumulative_response():
    district_cumulative_response = [
        {
            "district_id": 1,
            "name": "district_1",
            "date_wise_details": [
                {
                    "till_date": "2020/05/26",
                    "total_confirmed": 200,
                    "total_deaths": 30,
                    "total_recovered": 110,
                    "total_active": 60,
                },
                {
                    "till_date": "2020/05/27",
                    "total_confirmed": 200,
                    "total_deaths": 30,
                    "total_recovered": 140,
                    "total_active": 30,
                }
            ]
        },
        {
            "district_id": 2,
            "name": "district_2",
            "date_wise_details": [
                {
                    "till_date": "2020/05/26",
                    "total_confirmed": 200,
                    "total_deaths": 45,
                    "total_recovered": 65,
                    "total_active": 90,
                },
                {
                    "till_date": "2020/05/27",
                    "total_confirmed": 200,
                    "total_deaths": 15,
                    "total_recovered": 80,
                    "total_active": 105,
                }
            ]
        }
    ]
    return district_cumulative_response

@pytest.fixture()
def state_statistics_response():
    state_statistics_response = {
        "name": "state_1",
        "total_confirmed": 400,
        "total_deaths": 75,
        "total_recovered": 175,
        "districts": [
            {
                "district_id": 1,
                "name": "district_1",
                "total_confirmed": 200,
                "total_deaths": 30,
                "total_recovered": 110
            },
            {
                "district_id": 2,
                "name": "district_2",
                "total_confirmed": 200,
                "total_deaths": 45,
                "total_recovered": 65
            }
        ]
    }

    return state_statistics_response

@pytest.fixture()
def district_cumulative_statistics_response():
    district_cumulative_statistics_response = {
        "name": "district_1",
        "total_confirmed": 400,
        "total_deaths": 60,
        "total_recovered": 250,
        "total_active": 90,
        "districts": [
            {
                "mandal_id": 1,
                "name": "mandal_1",
                "total_confirmed": 200,
                "total_deaths": 20,
                "total_recovered": 150,
                "total_active": 30
            },
            {
                "mandal_id": 2,
                "name": "mandal_2",
                "total_confirmed": 200,
                "total_deaths": 40,
                "total_recovered": 100,
                "total_active": 60
            }
        ]
    }
    return district_cumulative_statistics_response

@pytest.fixture()
def get_daily_statistics_response():
    get_daily_statistics_response = [
        {
            "for_date": "2020/05/27",
            "district_id": 1,
            "district_name": "district_1",
            "mandal_id": 1,
            "mandal_name": "mandal_1",
            "total_confirmed": 20,
            "total_deaths": 2,
            "total_recovered": 10
        }
    ]
    return get_daily_statistics_response

@pytest.fixture()
def day_wise_mandals_cumulative_response():
    mandals_cumulative_response = [
        {
            "mandal_id": 1,
            "name": "mandal_1",
            "date_wise_details": [
                {
                    "till_date": "2020/05/26",
                    "total_confirmed": 100,
                    "total_deaths": 10,
                    "total_recovered": 40,
                    "total_active": 50,
                },
                {
                    "till_date": "2020/05/27",
                    "total_confirmed": 200,
                    "total_deaths": 30,
                    "total_recovered": 100,
                    "total_active": 70,
                }
            ]
        },
        {
            "mandal_id": 2,
            "name": "mandal_2",
            "date_wise_details": [
                {
                    "till_date": "2020/05/26",
                    "total_confirmed": 100,
                    "total_deaths": 10,
                    "total_recovered": 40,
                    "total_active": 50,
                },
                {
                    "till_date": "2020/05/27",
                    "total_confirmed": 200,
                    "total_deaths": 30,
                    "total_recovered": 100,
                    "total_active": 70,
                }
            ]
        }
    ]
    return mandals_cumulative_response
