# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetDailyStatisticsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetDailyStatisticsAPITestCase::test_case body'] = [
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '01/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '02/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '03/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '04/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '05/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '01/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '02/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '03/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '04/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '05/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '01/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '02/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '03/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '04/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '05/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '01/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '02/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '03/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '04/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '05/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '01/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '02/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '03/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '04/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '05/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '01/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '02/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '03/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '04/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '05/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '01/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '02/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '03/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '04/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '05/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '01/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '02/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '03/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '04/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '05/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '01/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '02/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '03/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '04/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '05/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '01/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '02/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '03/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '04/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '05/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    }
]

snapshots['TestCase02GetDailyStatisticsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '9279',
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

snapshots['TestCase02GetDailyStatisticsAPITestCase::test_case get_daily_statistics_response'] = [
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '01/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '02/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '03/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '04/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '05/06/2020',
        'mandal_id': 1,
        'mandal_name': 'mandal0',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '01/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '02/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '03/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '04/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 1,
        'district_name': 'district0',
        'for_date': '05/06/2020',
        'mandal_id': 2,
        'mandal_name': 'mandal1',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '01/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '02/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '03/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '04/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '05/06/2020',
        'mandal_id': 3,
        'mandal_name': 'mandal2',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '01/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '02/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '03/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '04/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 2,
        'district_name': 'district1',
        'for_date': '05/06/2020',
        'mandal_id': 4,
        'mandal_name': 'mandal3',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '01/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '02/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '03/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '04/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '05/06/2020',
        'mandal_id': 5,
        'mandal_name': 'mandal4',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '01/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '02/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '03/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '04/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 3,
        'district_name': 'district2',
        'for_date': '05/06/2020',
        'mandal_id': 6,
        'mandal_name': 'mandal5',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '01/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '02/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '03/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '04/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '05/06/2020',
        'mandal_id': 7,
        'mandal_name': 'mandal6',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '01/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '02/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '03/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '04/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 4,
        'district_name': 'district3',
        'for_date': '05/06/2020',
        'mandal_id': 8,
        'mandal_name': 'mandal7',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '01/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '02/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '03/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '04/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '05/06/2020',
        'mandal_id': 9,
        'mandal_name': 'mandal8',
        'total_confirmed': 500,
        'total_deaths': 80,
        'total_recovered': 30
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '01/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 600,
        'total_deaths': 90,
        'total_recovered': 40
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '02/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 700,
        'total_deaths': 100,
        'total_recovered': 50
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '03/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 800,
        'total_deaths': 150,
        'total_recovered': 100
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '04/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 300,
        'total_deaths': 60,
        'total_recovered': 10
    },
    {
        'district_id': 5,
        'district_name': 'district4',
        'for_date': '05/06/2020',
        'mandal_id': 10,
        'mandal_name': 'mandal9',
        'total_confirmed': 400,
        'total_deaths': 70,
        'total_recovered': 20
    }
]
