# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_state_stats_on_given_date"
REQUEST_METHOD = "post"
URL_SUFFIX = "state/for_date/statistics/v1/"

from .test_case_01 import TestCase01GetStateStatsOnGivenDateAPITestCase

__all__ = [
    "TestCase01GetStateStatsOnGivenDateAPITestCase"
]
