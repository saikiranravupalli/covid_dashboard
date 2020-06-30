# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetCumulativeDistrictDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetCumulativeDistrictDetailsAPITestCase::test_case body'] = {
    'mandals': [
        {
            'mandal_id': 1,
            'name': 'mandal0',
            'total_active': 930,
            'total_confirmed': 1200,
            'total_deaths': 60,
            'total_recovered': 210
        },
        {
            'mandal_id': 2,
            'name': 'mandal1',
            'total_active': 1090,
            'total_confirmed': 1500,
            'total_deaths': 130,
            'total_recovered': 280
        }
    ],
    'name': 'district0',
    'total_active': 2020,
    'total_confirmed': 2700,
    'total_deaths': 190,
    'total_recovered': 490
}

snapshots['TestCase02GetCumulativeDistrictDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '382',
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

snapshots['TestCase02GetCumulativeDistrictDetailsAPITestCase::test_case get_cumulative_district_details_response'] = {
    'mandals': [
        {
            'mandal_id': 1,
            'name': 'mandal0',
            'total_active': 930,
            'total_confirmed': 1200,
            'total_deaths': 60,
            'total_recovered': 210
        },
        {
            'mandal_id': 2,
            'name': 'mandal1',
            'total_active': 1090,
            'total_confirmed': 1500,
            'total_deaths': 130,
            'total_recovered': 280
        }
    ],
    'name': 'district0',
    'total_active': 2020,
    'total_confirmed': 2700,
    'total_deaths': 190,
    'total_recovered': 490
}
