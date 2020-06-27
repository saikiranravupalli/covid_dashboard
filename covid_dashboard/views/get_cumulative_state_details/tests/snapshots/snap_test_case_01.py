# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCumulativeStateDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetCumulativeStateDetailsAPITestCase::test_case body'] = {
    'districts': [
        {
            'district_id': 1,
            'name': 'district0',
            'total_active': 2020,
            'total_confirmed': 2700,
            'total_deaths': 190,
            'total_recovered': 490
        },
        {
            'district_id': 2,
            'name': 'district1',
            'total_active': 2900,
            'total_confirmed': 3900,
            'total_deaths': 350,
            'total_recovered': 650
        },
        {
            'district_id': 3,
            'name': 'district2',
            'total_active': 2580,
            'total_confirmed': 3300,
            'total_deaths': 210,
            'total_recovered': 510
        },
        {
            'district_id': 4,
            'name': 'district3',
            'total_active': 2020,
            'total_confirmed': 2700,
            'total_deaths': 190,
            'total_recovered': 490
        },
        {
            'district_id': 5,
            'name': 'district4',
            'total_active': 2900,
            'total_confirmed': 3900,
            'total_deaths': 350,
            'total_recovered': 650
        }
    ],
    'name': 'state0',
    'total_active': 12420,
    'total_confirmed': 16500,
    'total_deaths': 1290,
    'total_recovered': 2790
}

snapshots['TestCase01GetCumulativeStateDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '794',
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

snapshots['TestCase01GetCumulativeStateDetailsAPITestCase::test_case get_cumulative_state_details_response'] = {
    'districts': [
        {
            'district_id': 1,
            'name': 'district0',
            'total_active': 2020,
            'total_confirmed': 2700,
            'total_deaths': 190,
            'total_recovered': 490
        },
        {
            'district_id': 2,
            'name': 'district1',
            'total_active': 2900,
            'total_confirmed': 3900,
            'total_deaths': 350,
            'total_recovered': 650
        },
        {
            'district_id': 3,
            'name': 'district2',
            'total_active': 2580,
            'total_confirmed': 3300,
            'total_deaths': 210,
            'total_recovered': 510
        },
        {
            'district_id': 4,
            'name': 'district3',
            'total_active': 2020,
            'total_confirmed': 2700,
            'total_deaths': 190,
            'total_recovered': 490
        },
        {
            'district_id': 5,
            'name': 'district4',
            'total_active': 2900,
            'total_confirmed': 3900,
            'total_deaths': 350,
            'total_recovered': 650
        }
    ],
    'name': 'state0',
    'total_active': 12420,
    'total_confirmed': 16500,
    'total_deaths': 1290,
    'total_recovered': 2790
}
