# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetMandalsDayWiseCumulativeStatisticsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetMandalsDayWiseCumulativeStatisticsAPITestCase::test_case body'] = [
    {
        'date_wise_details': [
            {
                'till_date': '01/06/2020',
                'total_active': 230,
                'total_confirmed': 300,
                'total_deaths': 10,
                'total_recovered': 60
            },
            {
                'till_date': '02/06/2020',
                'total_active': 540,
                'total_confirmed': 700,
                'total_deaths': 30,
                'total_recovered': 130
            },
            {
                'till_date': '03/06/2020',
                'total_active': 930,
                'total_confirmed': 1200,
                'total_deaths': 60,
                'total_recovered': 210
            },
            {
                'till_date': '04/06/2020',
                'total_active': 1400,
                'total_confirmed': 1800,
                'total_deaths': 100,
                'total_recovered': 300
            },
            {
                'till_date': '05/06/2020',
                'total_active': 1950,
                'total_confirmed': 2500,
                'total_deaths': 150,
                'total_recovered': 400
            }
        ],
        'mandal_id': 1,
        'name': 'mandal0'
    },
    {
        'date_wise_details': [
            {
                'till_date': '01/06/2020',
                'total_active': 550,
                'total_confirmed': 800,
                'total_deaths': 100,
                'total_recovered': 150
            },
            {
                'till_date': '02/06/2020',
                'total_active': 780,
                'total_confirmed': 1100,
                'total_deaths': 110,
                'total_recovered': 210
            },
            {
                'till_date': '03/06/2020',
                'total_active': 1090,
                'total_confirmed': 1500,
                'total_deaths': 130,
                'total_recovered': 280
            },
            {
                'till_date': '04/06/2020',
                'total_active': 1480,
                'total_confirmed': 2000,
                'total_deaths': 160,
                'total_recovered': 360
            },
            {
                'till_date': '05/06/2020',
                'total_active': 1950,
                'total_confirmed': 2600,
                'total_deaths': 200,
                'total_recovered': 450
            }
        ],
        'mandal_id': 2,
        'name': 'mandal1'
    }
]

snapshots['TestCase02GetMandalsDayWiseCumulativeStatisticsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1318',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots['TestCase02GetMandalsDayWiseCumulativeStatisticsAPITestCase::test_case get_mandals_day_wise_cumulative_statistics_response'] = [
    {
        'date_wise_details': [
            {
                'till_date': '01/06/2020',
                'total_active': 230,
                'total_confirmed': 300,
                'total_deaths': 10,
                'total_recovered': 60
            },
            {
                'till_date': '02/06/2020',
                'total_active': 540,
                'total_confirmed': 700,
                'total_deaths': 30,
                'total_recovered': 130
            },
            {
                'till_date': '03/06/2020',
                'total_active': 930,
                'total_confirmed': 1200,
                'total_deaths': 60,
                'total_recovered': 210
            },
            {
                'till_date': '04/06/2020',
                'total_active': 1400,
                'total_confirmed': 1800,
                'total_deaths': 100,
                'total_recovered': 300
            },
            {
                'till_date': '05/06/2020',
                'total_active': 1950,
                'total_confirmed': 2500,
                'total_deaths': 150,
                'total_recovered': 400
            }
        ],
        'mandal_id': 1,
        'name': 'mandal0'
    },
    {
        'date_wise_details': [
            {
                'till_date': '01/06/2020',
                'total_active': 550,
                'total_confirmed': 800,
                'total_deaths': 100,
                'total_recovered': 150
            },
            {
                'till_date': '02/06/2020',
                'total_active': 780,
                'total_confirmed': 1100,
                'total_deaths': 110,
                'total_recovered': 210
            },
            {
                'till_date': '03/06/2020',
                'total_active': 1090,
                'total_confirmed': 1500,
                'total_deaths': 130,
                'total_recovered': 280
            },
            {
                'till_date': '04/06/2020',
                'total_active': 1480,
                'total_confirmed': 2000,
                'total_deaths': 160,
                'total_recovered': 360
            },
            {
                'till_date': '05/06/2020',
                'total_active': 1950,
                'total_confirmed': 2600,
                'total_deaths': 200,
                'total_recovered': 450
            }
        ],
        'mandal_id': 2,
        'name': 'mandal1'
    }
]
