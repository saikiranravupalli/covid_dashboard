# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDayWiseCumulativeMandalDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetDayWiseCumulativeMandalDetailsAPITestCase::test_case body'] = {
    'date_wise_details': [
        {
            'till_date': '01/06/2020',
            'total_active': 780,
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        },
        {
            'till_date': '02/06/2020',
            'total_active': 1320,
            'total_confirmed': 1800,
            'total_deaths': 140,
            'total_recovered': 340
        },
        {
            'till_date': '03/06/2020',
            'total_active': 2020,
            'total_confirmed': 2700,
            'total_deaths': 190,
            'total_recovered': 490
        },
        {
            'till_date': '04/06/2020',
            'total_active': 2880,
            'total_confirmed': 3800,
            'total_deaths': 260,
            'total_recovered': 660
        },
        {
            'till_date': '05/06/2020',
            'total_active': 3900,
            'total_confirmed': 5100,
            'total_deaths': 350,
            'total_recovered': 850
        }
    ],
    'name': 'district0'
}

snapshots['TestCase01GetDayWiseCumulativeMandalDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '648',
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

snapshots['TestCase01GetDayWiseCumulativeMandalDetailsAPITestCase::test_case get_day_wise_cumulative_mandal_details_response'] = {
    'date_wise_details': [
        {
            'till_date': '01/06/2020',
            'total_active': 780,
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        },
        {
            'till_date': '02/06/2020',
            'total_active': 1320,
            'total_confirmed': 1800,
            'total_deaths': 140,
            'total_recovered': 340
        },
        {
            'till_date': '03/06/2020',
            'total_active': 2020,
            'total_confirmed': 2700,
            'total_deaths': 190,
            'total_recovered': 490
        },
        {
            'till_date': '04/06/2020',
            'total_active': 2880,
            'total_confirmed': 3800,
            'total_deaths': 260,
            'total_recovered': 660
        },
        {
            'till_date': '05/06/2020',
            'total_active': 3900,
            'total_confirmed': 5100,
            'total_deaths': 350,
            'total_recovered': 850
        }
    ],
    'name': 'district0'
}
