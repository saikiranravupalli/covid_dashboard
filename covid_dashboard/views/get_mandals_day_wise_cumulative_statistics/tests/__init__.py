# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_mandals_day_wise_cumulative_statistics"
REQUEST_METHOD = "get"
URL_SUFFIX = "districts/{district_id}/mandals/day_wise/cumulative/v1/"

from .test_case_01 import TestCase01GetMandalsDayWiseCumulativeStatisticsAPITestCase

__all__ = [
    "TestCase01GetMandalsDayWiseCumulativeStatisticsAPITestCase"
]
