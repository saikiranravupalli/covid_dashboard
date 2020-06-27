# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetDayWiseDistrictDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetDayWiseDistrictDetailsAPITestCase::test_case body'] = {
    'day_wise_details': [
        {
            'for_date': '01/06/2020',
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        },
        {
            'for_date': '02/06/2020',
            'total_confirmed': 700,
            'total_deaths': 30,
            'total_recovered': 130
        },
        {
            'for_date': '03/06/2020',
            'total_confirmed': 900,
            'total_deaths': 50,
            'total_recovered': 150
        },
        {
            'for_date': '04/06/2020',
            'total_confirmed': 1100,
            'total_deaths': 70,
            'total_recovered': 170
        },
        {
            'for_date': '05/06/2020',
            'total_confirmed': 1300,
            'total_deaths': 90,
            'total_recovered': 190
        }
    ],
    'name': 'district0'
}

snapshots['TestCase02GetDayWiseDistrictDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '527',
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

snapshots['TestCase02GetDayWiseDistrictDetailsAPITestCase::test_case get_day_wise_district_details_response'] = {
    'day_wise_details': [
        {
            'for_date': '01/06/2020',
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        },
        {
            'for_date': '02/06/2020',
            'total_confirmed': 700,
            'total_deaths': 30,
            'total_recovered': 130
        },
        {
            'for_date': '03/06/2020',
            'total_confirmed': 900,
            'total_deaths': 50,
            'total_recovered': 150
        },
        {
            'for_date': '04/06/2020',
            'total_confirmed': 1100,
            'total_deaths': 70,
            'total_recovered': 170
        },
        {
            'for_date': '05/06/2020',
            'total_confirmed': 1300,
            'total_deaths': 90,
            'total_recovered': 190
        }
    ],
    'name': 'district0'
}
