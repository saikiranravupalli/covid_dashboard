# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStateDayWiseCumulativeReportDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetStateDayWiseCumulativeReportDetailsAPITestCase::test_case body'] = {
    'date_wise_details': [
        {
            'till_date': '01/06/2020',
            'total_active': 4300,
            'total_confirmed': 5700,
            'total_deaths': 450,
            'total_recovered': 950
        },
        {
            'till_date': '02/06/2020',
            'total_active': 8440,
            'total_confirmed': 11200,
            'total_deaths': 880,
            'total_recovered': 1880
        },
        {
            'till_date': '03/06/2020',
            'total_active': 12420,
            'total_confirmed': 16500,
            'total_deaths': 1290,
            'total_recovered': 2790
        },
        {
            'till_date': '04/06/2020',
            'total_active': 16320,
            'total_confirmed': 21600,
            'total_deaths': 1640,
            'total_recovered': 3640
        },
        {
            'till_date': '05/06/2020',
            'total_active': 20540,
            'total_confirmed': 27100,
            'total_deaths': 2030,
            'total_recovered': 4530
        }
    ],
    'name': 'state0'
}

snapshots['TestCase01GetStateDayWiseCumulativeReportDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '660',
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

snapshots['TestCase01GetStateDayWiseCumulativeReportDetailsAPITestCase::test_case get_state_day_wise_cumulative_report_details_response'] = {
    'date_wise_details': [
        {
            'till_date': '01/06/2020',
            'total_active': 4300,
            'total_confirmed': 5700,
            'total_deaths': 450,
            'total_recovered': 950
        },
        {
            'till_date': '02/06/2020',
            'total_active': 8440,
            'total_confirmed': 11200,
            'total_deaths': 880,
            'total_recovered': 1880
        },
        {
            'till_date': '03/06/2020',
            'total_active': 12420,
            'total_confirmed': 16500,
            'total_deaths': 1290,
            'total_recovered': 2790
        },
        {
            'till_date': '04/06/2020',
            'total_active': 16320,
            'total_confirmed': 21600,
            'total_deaths': 1640,
            'total_recovered': 3640
        },
        {
            'till_date': '05/06/2020',
            'total_active': 20540,
            'total_confirmed': 27100,
            'total_deaths': 2030,
            'total_recovered': 4530
        }
    ],
    'name': 'state0'
}
