# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case status'] = 201

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case body'] = b''

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '0',
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

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case mandal_id'] = 1

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case for_date'] = '01/06/2020'

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case total_confirmed'] = 1

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case total_recovered'] = 1

snapshots['TestCase05CreateOrUpdateMandalStatisticsAPITestCase::test_case total_deaths'] = 1
