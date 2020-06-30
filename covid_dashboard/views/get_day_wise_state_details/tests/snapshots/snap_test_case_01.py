# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDayWiseStateDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetDayWiseStateDetailsAPITestCase::test_case body'] = {
    'day_wise_details': [
        {
            'for_date': '01/06/2020',
            'total_confirmed': 5700,
            'total_deaths': 450,
            'total_recovered': 950
        },
        {
            'for_date': '02/06/2020',
            'total_confirmed': 5500,
            'total_deaths': 430,
            'total_recovered': 930
        },
        {
            'for_date': '03/06/2020',
            'total_confirmed': 5300,
            'total_deaths': 410,
            'total_recovered': 910
        },
        {
            'for_date': '04/06/2020',
            'total_confirmed': 5100,
            'total_deaths': 350,
            'total_recovered': 850
        },
        {
            'for_date': '05/06/2020',
            'total_confirmed': 5500,
            'total_deaths': 390,
            'total_recovered': 890
        }
    ],
    'name': 'state0'
}

snapshots['TestCase01GetDayWiseStateDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '530',
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

snapshots['TestCase01GetDayWiseStateDetailsAPITestCase::test_case get_day_wise_state_details_response'] = {
    'day_wise_details': [
        {
            'for_date': '01/06/2020',
            'total_confirmed': 5700,
            'total_deaths': 450,
            'total_recovered': 950
        },
        {
            'for_date': '02/06/2020',
            'total_confirmed': 5500,
            'total_deaths': 430,
            'total_recovered': 930
        },
        {
            'for_date': '03/06/2020',
            'total_confirmed': 5300,
            'total_deaths': 410,
            'total_recovered': 910
        },
        {
            'for_date': '04/06/2020',
            'total_confirmed': 5100,
            'total_deaths': 350,
            'total_recovered': 850
        },
        {
            'for_date': '05/06/2020',
            'total_confirmed': 5500,
            'total_deaths': 390,
            'total_recovered': 890
        }
    ],
    'name': 'state0'
}
