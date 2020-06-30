# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetDistrictStatsOnGivenDateAPITestCase::test_case status'] = 200

snapshots['TestCase02GetDistrictStatsOnGivenDateAPITestCase::test_case body'] = {
    'mandals': [
        {
            'mandal_id': 1,
            'name': 'mandal0',
            'total_confirmed': 500,
            'total_deaths': 30,
            'total_recovered': 80
        },
        {
            'mandal_id': 2,
            'name': 'mandal1',
            'total_confirmed': 400,
            'total_deaths': 20,
            'total_recovered': 70
        }
    ],
    'name': 'district0',
    'total_confirmed': 900,
    'total_deaths': 50,
    'total_recovered': 150
}

snapshots['TestCase02GetDistrictStatsOnGivenDateAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '310',
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

snapshots['TestCase02GetDistrictStatsOnGivenDateAPITestCase::test_case get_district_stats_on_given_date_response'] = {
    'mandals': [
        {
            'mandal_id': 1,
            'name': 'mandal0',
            'total_confirmed': 500,
            'total_deaths': 30,
            'total_recovered': 80
        },
        {
            'mandal_id': 2,
            'name': 'mandal1',
            'total_confirmed': 400,
            'total_deaths': 20,
            'total_recovered': 70
        }
    ],
    'name': 'district0',
    'total_confirmed': 900,
    'total_deaths': 50,
    'total_recovered': 150
}
