# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStateStatsOnGivenDateAPITestCase::test_case status'] = 200

snapshots['TestCase01GetStateStatsOnGivenDateAPITestCase::test_case body'] = {
    'districts': [
        {
            'district_id': 1,
            'name': 'district0',
            'total_confirmed': 900,
            'total_deaths': 50,
            'total_recovered': 150
        },
        {
            'district_id': 2,
            'name': 'district1',
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        },
        {
            'district_id': 3,
            'name': 'district2',
            'total_confirmed': 1300,
            'total_deaths': 90,
            'total_recovered': 190
        },
        {
            'district_id': 4,
            'name': 'district3',
            'total_confirmed': 900,
            'total_deaths': 50,
            'total_recovered': 150
        },
        {
            'district_id': 5,
            'name': 'district4',
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        }
    ],
    'name': 'state0',
    'total_confirmed': 5300,
    'total_deaths': 410,
    'total_recovered': 910
}

snapshots['TestCase01GetStateStatsOnGivenDateAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '653',
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

snapshots['TestCase01GetStateStatsOnGivenDateAPITestCase::test_case get_state_stats_on_given_date_response'] = {
    'districts': [
        {
            'district_id': 1,
            'name': 'district0',
            'total_confirmed': 900,
            'total_deaths': 50,
            'total_recovered': 150
        },
        {
            'district_id': 2,
            'name': 'district1',
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        },
        {
            'district_id': 3,
            'name': 'district2',
            'total_confirmed': 1300,
            'total_deaths': 90,
            'total_recovered': 190
        },
        {
            'district_id': 4,
            'name': 'district3',
            'total_confirmed': 900,
            'total_deaths': 50,
            'total_recovered': 150
        },
        {
            'district_id': 5,
            'name': 'district4',
            'total_confirmed': 1100,
            'total_deaths': 110,
            'total_recovered': 210
        }
    ],
    'name': 'state0',
    'total_confirmed': 5300,
    'total_deaths': 410,
    'total_recovered': 910
}
