# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetMandalsDayWiseCumulativeStatisticsAPITestCase::test_case status'] = 400

snapshots['TestCase01GetMandalsDayWiseCumulativeStatisticsAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DISTRICT_ID',
    'response': 'Invalid district_id, try with valid district id'
}

snapshots['TestCase01GetMandalsDayWiseCumulativeStatisticsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '125',
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
