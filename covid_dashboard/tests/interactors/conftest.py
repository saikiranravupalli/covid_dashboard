from datetime import datetime
import pytest
from typing import List

from covid_dashboard.interactors.storages.dtos import \
    StateCumulativeStatisticsDto, DistrictStatisticsDto, \
    StateDayWiseCumulativeStatisticsDto, DistrictDayWiseStatisticsDto, \
    DistrictsDayWiseCumulativeStatisticsDto, DistrictActiveCasesDto, \
    StateStatisticsDto, MandalActiveCasesDto, DistrictCumulativeStatisticsDto,\
    DailyStatisticsDto, DistrictDayWiseCumulativeStatisticsDto, \
    MandalStatisticsDto, DistrictOnDateStatisticsDto, \
    MandalDayWiseStatisticsDto, MandalsDayWiseCumulativeStatisticsDto, \
    DistrictDailyStatisticsDto

@pytest.fixture()
def districts_dto():
    districts_dto = [
        DistrictActiveCasesDto(
            district_id=1,
            name='District_1',
            total_confirmed=100,
            total_deaths=10,
            total_recovered=30,
            total_active=60
        ),
        DistrictActiveCasesDto(
            district_id=2,
            name='District_2',
            total_confirmed=120,
            total_deaths=20,
            total_recovered=50,
            total_active=50
        )
    ]
    return districts_dto

@pytest.fixture()
def state_cumulative_dto():
    state_cumulative_dto = \
        StateCumulativeStatisticsDto(
            name="State_1",
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            total_active=110,
            districts=districts_dto
        )

    return state_cumulative_dto

@pytest.fixture()
def state_day_wise_cumulative_dto():
    state_day_wise_cumulative_dto = [
        StateDayWiseCumulativeStatisticsDto(
            name="State_1",
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            total_active=110,
        ),
        StateDayWiseCumulativeStatisticsDto(
            name="State_1",
            till_date=datetime(2020, 5, 28).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            total_active=110,
        ),
        StateDayWiseCumulativeStatisticsDto(
            name="State_1",
            till_date=datetime(2020, 5, 29).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            total_active=110,
        )
    ]
    return state_day_wise_cumulative_dto

@pytest.fixture()
def district_day_wise_cumulative_dto():
    district_day_wise_cumulative_dto = \
        DistrictDayWiseCumulativeStatisticsDto(
            name="district_1",
            date_wise_details=[
                DistrictDayWiseStatisticsDto(
                    till_date=datetime(2020, 5, 27).date(),
                    total_confirmed=220,
                    total_deaths=30,
                    total_recovered=80,
                    total_active=110,
                ),
                DistrictDayWiseStatisticsDto(
                    till_date=datetime(2020, 5, 28).date(),
                    total_confirmed=220,
                    total_deaths=30,
                    total_recovered=80,
                    total_active=110,
                ),
                DistrictDayWiseStatisticsDto(
                    till_date=datetime(2020, 5, 29).date(),
                    total_confirmed=220,
                    total_deaths=30,
                    total_recovered=80,
                    total_active=110,
                )
            ]
        )
    return district_day_wise_cumulative_dto

@pytest.fixture()
def updated_state_day_wise_cumulative_dto():
    state_day_wise_cumulative_dto = [
        StateDayWiseCumulativeStatisticsDto(
            name="State_1",
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            total_active=110,
        ),
        StateDayWiseCumulativeStatisticsDto(
            name="State_1",
            till_date=datetime(2020, 5, 28).date(),
            total_confirmed=440,
            total_deaths=60,
            total_recovered=160,
            total_active=220,
        ),
        StateDayWiseCumulativeStatisticsDto(
            name="State_1",
            till_date=datetime(2020, 5, 29).date(),
            total_confirmed=660,
            total_deaths=90,
            total_recovered=240,
            total_active=330,
        )
    ]
    return state_day_wise_cumulative_dto

@pytest.fixture()
def updated_district_day_wise_cumulative_dto():
    district_day_wise_cumulative_dto = \
        DistrictDayWiseCumulativeStatisticsDto(
            name="district_1",
            date_wise_details=[
                DistrictDayWiseStatisticsDto(
                    till_date=datetime(2020, 5, 27).date(),
                    total_confirmed=220,
                    total_deaths=30,
                    total_recovered=80,
                    total_active=110,
                ),
                DistrictDayWiseStatisticsDto(
                    till_date=datetime(2020, 5, 28).date(),
                    total_confirmed=440,
                    total_deaths=60,
                    total_recovered=160,
                    total_active=220,
                ),
                DistrictDayWiseStatisticsDto(
                    till_date=datetime(2020, 5, 29).date(),
                    total_confirmed=660,
                    total_deaths=90,
                    total_recovered=240,
                    total_active=330,
                )
            ]
        )
    return district_day_wise_cumulative_dto

@pytest.fixture()
def district1_day_wise_stats():
    district_day_wise_stats = [
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=100,
            total_deaths=20,
            total_recovered=60,
            total_active=20
        )
    ]
    return district_day_wise_stats

@pytest.fixture()
def district1_day_wise_cumulative_stats():
    district_day_wise_cumulative_stats = [
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=100,
            total_active=70
        )
    ]
    return district_day_wise_cumulative_stats

@pytest.fixture()
def district2_day_wise_stats():
    district_day_wise_stats = [
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=100,
            total_deaths=20,
            total_recovered=60,
            total_active=20
        )
    ]
    return district_day_wise_stats

@pytest.fixture()
def district2_day_wise_cumulative_stats():
    district_day_wise_cumulative_stats = [
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        DistrictDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=200,
            total_deaths=30,
            total_recovered=100,
            total_active=70
        )
    ]
    return district_day_wise_cumulative_stats

@pytest.fixture()
def districts_day_wise_stats(district1_day_wise_stats,
                             district2_day_wise_stats):

    districts_day_wise_cumulative_stats = [
        DistrictsDayWiseCumulativeStatisticsDto(
            district_id=1,
            name='district_1',
            date_wise_details = district1_day_wise_stats
        ),
        DistrictsDayWiseCumulativeStatisticsDto(
            district_id=2,
            name='district_2',
            date_wise_details = district2_day_wise_stats
        )
    ]

    return districts_day_wise_cumulative_stats

@pytest.fixture()
def districts_day_wise_cumulative_stats(district1_day_wise_cumulative_stats,
                                        district2_day_wise_cumulative_stats):

    districts_day_wise_cumulative_stats = [
        DistrictsDayWiseCumulativeStatisticsDto(
            district_id=1,
            name='district_1',
            date_wise_details = district1_day_wise_cumulative_stats
        ),
        DistrictsDayWiseCumulativeStatisticsDto(
            district_id=2,
            name='district_2',
            date_wise_details = district2_day_wise_cumulative_stats
        )
    ]

    return districts_day_wise_cumulative_stats

@pytest.fixture()
def district_statisticts_dto():
    districts_dto = [
        DistrictStatisticsDto(
            district_id=1,
            name='District_1',
            total_confirmed=100,
            total_deaths=10,
            total_recovered=30
        ),
        DistrictStatisticsDto(
            district_id=2,
            name='District_2',
            total_confirmed=120,
            total_deaths=20,
            total_recovered=50
        )
    ]
    return districts_dto

@pytest.fixture()
def mandal_statisticts_dto():
    mandals_dto = [
        MandalStatisticsDto(
            mandal_id=1,
            name='mandal_1',
            total_confirmed=100,
            total_deaths=10,
            total_recovered=30
        ),
        MandalStatisticsDto(
            mandal_id=2,
            name='mandal_2',
            total_confirmed=120,
            total_deaths=20,
            total_recovered=50
        )
    ]
    return mandals_dto

@pytest.fixture()
def state_statistics_dto(district_statisticts_dto):
    state_statistics_dto = \
        StateStatisticsDto(
            name="State_1",
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            districts=district_statisticts_dto
        )

    return state_statistics_dto

@pytest.fixture()
def district_statistics_dto(mandal_statisticts_dto):
    district_statistics_dto = \
        DistrictOnDateStatisticsDto(
            name="district_1",
            total_confirmed=220,
            total_deaths=30,
            total_recovered=80,
            mandals=mandal_statisticts_dto
        )

    return district_statistics_dto

@pytest.fixture()
def mandals_active_cases_dto():
    mandals_active_cases_dto = [
        MandalActiveCasesDto(
            mandal_id=1,
            name='mandal_1',
            total_confirmed=50,
            total_deaths=10,
            total_recovered=20,
            total_active=20
        ),
        MandalActiveCasesDto(
            mandal_id=2,
            name='mandal_2',
            total_confirmed=100,
            total_deaths=20,
            total_recovered=40,
            total_active=40
        )
    ]
    return mandals_active_cases_dto

@pytest.fixture()
def district_cumulative_statistics_dto(mandals_active_cases_dto):
    district_cumulative_statistics_dto = \
        DistrictCumulativeStatisticsDto(
            name='district_1',
            total_confirmed=150,
            total_deaths=30,
            total_recovered=60,
            total_active=60,
            mandals=mandals_active_cases_dto
        )
    return district_cumulative_statistics_dto

@pytest.fixture()
def state_day_wise_statistics_dtos(state_day_wise_cumulative_dto):
    state_day_wise_statistics_dtos = state_day_wise_cumulative_dto
    return state_day_wise_statistics_dtos

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
def mandal1_day_wise_stats():
    mandal_day_wise_stats = [
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=100,
            total_deaths=20,
            total_recovered=60,
            total_active=20
        )
    ]
    return mandal_day_wise_stats

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
def mandal2_day_wise_stats():
    mandal_day_wise_stats = [
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=100,
            total_deaths=10,
            total_recovered=40,
            total_active=50
        ),
        MandalDayWiseStatisticsDto(
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=100,
            total_deaths=20,
            total_recovered=60,
            total_active=20
        )
    ]
    return mandal_day_wise_stats

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
def mandals_day_wise_stats(mandal1_day_wise_stats,
                           mandal2_day_wise_stats):

    mandals_day_wise_cumulative_stats = [
        MandalsDayWiseCumulativeStatisticsDto(
            mandal_id=1,
            name='mandal_1',
            date_wise_details = mandal1_day_wise_stats
        ),
        MandalsDayWiseCumulativeStatisticsDto(
            mandal_id=2,
            name='mandal_2',
            date_wise_details = mandal2_day_wise_stats
        )
    ]

    return mandals_day_wise_cumulative_stats

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
def district_day_wise_details_dtos():
    district_day_wise_details_dtos = [
        DistrictDailyStatisticsDto(
            name='district_1',
            till_date=datetime(2020, 5, 27).date(),
            total_confirmed=10,
            total_deaths=2,
            total_recovered=30,
        ),
        DistrictDailyStatisticsDto(
            name='district_1',
            till_date=datetime(2020, 5, 26).date(),
            total_confirmed=30,
            total_deaths=20,
            total_recovered=10
        )
    ]
    return district_day_wise_details_dtos

@pytest.fixture()
def state_cumulative_response():
    state_cumulative_response = {
        "name": "State_1",
        "total_confirmed": 220,
        "total_deaths": 30,
        "total_recovered": 80,
        "total_active": 110,
        "districts": [
            {
                "district_id": 1,
                "name": "District_1",
                "total_confirmed": 100,
                "total_deaths": 10,
                "total_recovered": 30,
                "total_active": 60
            },
            {
                "district_id": 2,
                "name": "District_2",
                "total_confirmed": 120,
                "total_deaths": 20,
                "total_recovered": 50,
                "total_active": 50
            }
        ]
    }
    return state_cumulative_response

@pytest.fixture()
def day_wise_state_statistics_response():
    state_statistics_response = {
        "name": "State_1",
        "day_wise_statistics": [
            {
                "till_date": "27/05/2020",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80,
                "total_active": 110,
            },
            {
                "till_date": "28/05/2020",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80,
                "total_active": 110,
            },
            {
                "till_date": "29/05/2020",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80,
                "total_active": 110,
            }
        ]
    }
    return state_statistics_response

@pytest.fixture()
def day_wise_state_cumulative_response():
    state_cumulative_response = {
        "name": "State_1",
        "day_wise_statistics": [
            {
                "till_date": "27/05/2020",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80,
                "total_active": 110,
            },
            {
                "till_date": "28/05/2020",
                "total_confirmed": 440,
                "total_deaths": 60,
                "total_recovered": 160,
                "total_active": 220,
            },
            {
                "till_date": "29/05/2020",
                "total_confirmed": 660,
                "total_deaths": 90,
                "total_recovered": 240,
                "total_active": 330,
            }
        ]
    }

    return state_cumulative_response

@pytest.fixture()
def day_wise_district_cumulative_response():
    district_cumulative_response = {
        "name": "district_1",
        "day_wise_details": [
            {
                "till_date": "27/05/2020",
                "total_confirmed": 220,
                "total_deaths": 30,
                "total_recovered": 80,
                "total_active": 110,
            },
            {
                "till_date": "28/05/2020",
                "total_confirmed": 440,
                "total_deaths": 60,
                "total_recovered": 160,
                "total_active": 220,
            },
            {
                "till_date": "29/05/2020",
                "total_confirmed": 660,
                "total_deaths": 90,
                "total_recovered": 240,
                "total_active": 330,
            }
        ]
    }

    return district_cumulative_response

@pytest.fixture()
def day_wise_districts_cumulative_response():
    district_cumulative_response = [
        {
            "district_id": 1,
            "name": "district_1",
            "date_wise_details": [
                {
                    "till_date": "26/05/2020",
                    "total_confirmed": 100,
                    "total_deaths": 10,
                    "total_recovered": 40,
                    "total_active": 50,
                },
                {
                    "till_date": "27/05/2020",
                    "total_confirmed": 200,
                    "total_deaths": 30,
                    "total_recovered": 100,
                    "total_active": 70,
                }
            ]
        },
        {
            "district_id": 2,
            "name": "district_2",
            "date_wise_details": [
                {
                    "till_date": "26/05/2020",
                    "total_confirmed": 100,
                    "total_deaths": 10,
                    "total_recovered": 40,
                    "total_active": 50,
                },
                {
                    "till_date": "27/05/2020",
                    "total_confirmed": 200,
                    "total_deaths": 30,
                    "total_recovered": 100,
                    "total_active": 70,
                }
            ]
        }
    ]
    return district_cumulative_response

@pytest.fixture()
def district_zone_details_response():
    district_zone_details_response = [
        {
            "district_id": 1,
            "name": "District_1",
            "zone": "GREEN"
        },
        {
            "district_id": 2,
            "name": "District_2",
            "zone": "ORANGE"
        },
        {
            "district_id": 3,
            "name": "District_3",
            "zone": "RED"
        }
    ]
    return district_zone_details_response

@pytest.fixture()
def state_statistics_response():
    state_statistics_response = {
        "name": "State_1",
        "total_confirmed": 220,
        "total_deaths": 30,
        "total_recovered": 80,
        "districts": [
            {
                "district_id": 1,
                "name": "District_1",
                "total_confirmed": 100,
                "total_deaths": 10,
                "total_recovered": 30
            },
            {
                "district_id": 2,
                "name": "District_2",
                "total_confirmed": 120,
                "total_deaths": 20,
                "total_recovered": 50
            }
        ]
    }

    return state_statistics_response

@pytest.fixture()
def district_day_wise_response():
    district_day_wise_response = {
        "name": "district_1",
        "date_wise_details": [
            {
                "for_date": "2020/05/26",
                "total_confirmed": 100,
                "total_recovered": 20,
                "total_deaths": 30
            },
            {
                "for_date": "2020/05/27",
                "total_confirmed": 200,
                "total_recovered": 20,
                "total_deaths": 30
            }
        ]
    }
    return district_day_wise_response

@pytest.fixture()
def district_statistics_response():
    district_statistics_response = {
        "name": "district_1",
        "total_confirmed": 220,
        "total_deaths": 30,
        "total_recovered": 80,
        "districts": [
            {
                "mandal_id": 1,
                "name": "mandal_1",
                "total_confirmed": 100,
                "total_deaths": 10,
                "total_recovered": 30
            },
            {
                "mandal_id": 2,
                "name": "mandal_2",
                "total_confirmed": 120,
                "total_deaths": 20,
                "total_recovered": 50
            }
        ]
    }

    return district_statistics_response

@pytest.fixture()
def district_cumulative_statistics_response():
    district_cumulative_statistics_response = {
        "name": "district_1",
        "total_confirmed": 150,
        "total_deaths": 30,
        "total_recovered": 60,
        "total_active": 60,
        "districts": [
            {
                "mandal_id": 1,
                "name": "mandal_1",
                "total_confirmed": 50,
                "total_deaths": 10,
                "total_recovered": 20,
                "total_active": 20
            },
            {
                "mandal_id": 2,
                "name": "mandal_2",
                "total_confirmed": 100,
                "total_deaths": 20,
                "total_recovered": 40,
                "total_active": 40
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

@pytest.fixture()
def district_daily_statistics_response():
    district_daily_statistics_response = {
        "name": "district_1",
        "date_wise_details": [
            {
                "name": "district_1",
                "till_date": "2020/5/26",
                "total_confirmed": 10,
                "total_recovered": 20,
                "total_deaths": 10
            },
            {
                "name": "district_1",
                "till_date": "2020/5/27",
                "total_confirmed": 30,
                "total_recovered": 10,
                "total_deaths": 10
            }
        ]
    }
    return district_daily_statistics_response
