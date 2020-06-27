# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserLoginDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetUserLoginDetailsAPITestCase::test_case body'] = {
    'access_token': 'wxJr6gRr9lB1zyv54SRXfK2BR88Ye3',
    'is_admin': False,
    'refresh_token': 'pOkxYG0LHI0TJwUh3AeQt9HUQldA5a'
}

snapshots['TestCase01GetUserLoginDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '120',
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
