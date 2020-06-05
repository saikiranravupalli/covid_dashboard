# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_district_stats_on_given_date"
REQUEST_METHOD = "post"
URL_SUFFIX = "districts/{district_id}/for_date/statistics/v1/"

from .test_case_01 import TestCase01GetDistrictStatsOnGivenDateAPITestCase

__all__ = [
    "TestCase01GetDistrictStatsOnGivenDateAPITestCase"
]
