from datetime import date
from covid_dashboard.models import State, District, \
    Mandal, DailyStatistics, User

users_list = [
    {
        "username": "user_1",
        "is_admin": True,
        "password": 123456
    },
    {
        "username": "user_2",
        "is_admin": False,
        "password": 654321
    }
]

districts_list =  [
    {
        "name": "Kurnool",
        "state_id": 1
    },
    {
        "name": "Guntur",
        "state_id": 1
    }
]

mandals_list = [
    {
        "name": "Nandyal",
        "district_id": 1
    },
    {
        "name": "Adoni",
        "district_id": 1
    },
    {
        "name": "Tenali",
        "district_id": 2
    },
    {
        "name": "Narasaraopeta",
        "district_id": 2
    }
]

daily_statistics_list = [
    {
        "for_date": date(2020, 6, 1),
        "total_confirmed": 40,
        "total_recovered": 20,
        "total_deaths": 5,
        "mandal_id": 1
    },
    {
        "for_date": date(2020, 6, 2),
        "total_confirmed": 50,
        "total_recovered": 30,
        "total_deaths": 10,
        "mandal_id": 1
    },
    {
        "for_date": date(2020, 6, 3),
        "total_confirmed": 60,
        "total_recovered": 40,
        "total_deaths": 15,
        "mandal_id": 1
    },
    {
        "for_date": date(2020, 6, 4),
        "total_confirmed": 100,
        "total_recovered": 20,
        "total_deaths": 15,
        "mandal_id": 1
    },
    {
        "for_date": date(2020, 6, 5),
        "total_confirmed": 140,
        "total_recovered": 50,
        "total_deaths": 25,
        "mandal_id": 1
    },
    {
        "for_date": date(2020, 6, 6),
        "total_confirmed": 150,
        "total_recovered": 40,
        "total_deaths": 15,
        "mandal_id": 1
    },
    {
        "for_date": date(2020, 6, 1),
        "total_confirmed": 100,
        "total_recovered": 30,
        "total_deaths": 15,
        "mandal_id": 2
    },
    {
        "for_date": date(2020, 6, 2),
        "total_confirmed": 120,
        "total_recovered": 40,
        "total_deaths": 20,
        "mandal_id": 2
    },
    {
        "for_date": date(2020, 6, 3),
        "total_confirmed": 140,
        "total_recovered": 60,
        "total_deaths": 25,
        "mandal_id": 2
    },
    {
        "for_date": date(2020, 6, 4),
        "total_confirmed": 120,
        "total_recovered": 40,
        "total_deaths": 45,
        "mandal_id": 2
    },
    {
        "for_date": date(2020, 6, 5),
        "total_confirmed": 60,
        "total_recovered": 20,
        "total_deaths": 5,
        "mandal_id": 2
    },
    {
        "for_date": date(2020, 6, 6),
        "total_confirmed": 135,
        "total_recovered": 70,
        "total_deaths": 25,
        "mandal_id": 2
    },
    {
        "for_date": date(2020, 6, 1),
        "total_confirmed": 200,
        "total_recovered": 40,
        "total_deaths": 30,
        "mandal_id": 3
    },
    {
        "for_date": date(2020, 6, 2),
        "total_confirmed": 250,
        "total_recovered": 80,
        "total_deaths": 40,
        "mandal_id": 3
    },
    {
        "for_date": date(2020, 6, 3),
        "total_confirmed": 300,
        "total_recovered": 100,
        "total_deaths": 40,
        "mandal_id": 3
    },
    {
        "for_date": date(2020, 6, 4),
        "total_confirmed": 125,
        "total_recovered": 45,
        "total_deaths": 20,
        "mandal_id": 3
    },
    {
        "for_date": date(2020, 6, 5),
        "total_confirmed": 160,
        "total_recovered": 35,
        "total_deaths": 20,
        "mandal_id": 3
    },
    {
        "for_date": date(2020, 6, 6),
        "total_confirmed": 260,
        "total_recovered": 100,
        "total_deaths": 15,
        "mandal_id": 3
    },
    {
        "for_date": date(2020, 6, 1),
        "total_confirmed": 400,
        "total_recovered": 120,
        "total_deaths": 30,
        "mandal_id": 4
    },
    {
        "for_date": date(2020, 6, 2),
        "total_confirmed": 500,
        "total_recovered": 130,
        "total_deaths": 25,
        "mandal_id": 4
    },
    {
        "for_date": date(2020, 6, 3),
        "total_confirmed": 600,
        "total_recovered": 140,
        "total_deaths": 20,
        "mandal_id": 4
    },
    {
        "for_date": date(2020, 6, 4),
        "total_confirmed": 270,
        "total_recovered": 90,
        "total_deaths": 20,
        "mandal_id": 4
    },
    {
        "for_date": date(2020, 6, 5),
        "total_confirmed": 70,
        "total_recovered": 130,
        "total_deaths": 15,
        "mandal_id": 4
    },
    {
        "for_date": date(2020, 6, 6),
        "total_confirmed": 200,
        "total_recovered": 80,
        "total_deaths": 5,
        "mandal_id": 4
    }
]

def populate_database():

    for user in users_list:
        created_user = User.objects.create(
            username=user['username'],
            is_admin=user['is_admin']
        )
        created_user.set_password(user['password'])
        created_user.save()

    State.objects.create(name="AndhraPradesh")

    districts = [
        District(
            name=district['name'],
            state_id=district['state_id']
        )
        for district in districts_list
    ]
    District.objects.bulk_create(districts)

    mandals = [
        Mandal(
            name=mandal['name'],
            district_id=mandal['district_id']
        )
        for mandal in mandals_list
    ]
    Mandal.objects.bulk_create(mandals)

    daily_statistics = [
        DailyStatistics(
            for_date=daily_stats['for_date'],
            total_confirmed=daily_stats['total_confirmed'],
            total_recovered=daily_stats['total_recovered'],
            total_deaths=daily_stats['total_deaths'],
            mandal_id=daily_stats['mandal_id']
        )
        for daily_stats in daily_statistics_list
    ]
    DailyStatistics.objects.bulk_create(daily_statistics)

# __author__ = 'ibhubs'


# class Fixture(object):
#     """
#     Class contains populate method as static method
#     Is used by django-swagger-utils as a management command
#     """

#     @staticmethod
#     def populate():
#         """
#         Populates data for app covid_dashboard
#         :return:
#         """
#         pass
