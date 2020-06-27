# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDistrictWiseZoneDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetDistrictWiseZoneDetailsAPITestCase::test_case body'] = [
    {
        'district_id': 1,
        'name': 'district0',
        'zone': 'GREEN'
    },
    {
        'district_id': 2,
        'name': 'district1',
        'zone': 'GREEN'
    },
    {
        'district_id': 3,
        'name': 'district2',
        'zone': 'GREEN'
    },
    {
        'district_id': 4,
        'name': 'district3',
        'zone': 'GREEN'
    },
    {
        'district_id': 5,
        'name': 'district4',
        'zone': 'GREEN'
    }
]

snapshots['TestCase01GetDistrictWiseZoneDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '290',
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

snapshots['TestCase01GetDistrictWiseZoneDetailsAPITestCase::test_case get_district_wise_zone_details_response'] = [
    {
        'district_id': 1,
        'name': 'district0',
        'zone': 'GREEN'
    },
    {
        'district_id': 2,
        'name': 'district1',
        'zone': 'GREEN'
    },
    {
        'district_id': 3,
        'name': 'district2',
        'zone': 'GREEN'
    },
    {
        'district_id': 4,
        'name': 'district3',
        'zone': 'GREEN'
    },
    {
        'district_id': 5,
        'name': 'district4',
        'zone': 'GREEN'
    }
]
