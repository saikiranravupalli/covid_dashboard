# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_day_wise_cumulative_mandal_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "districts/{district_id}/day_wise/cumulative/v1/"

from .test_case_01 import TestCase01GetDayWiseCumulativeMandalDetailsAPITestCase

__all__ = [
    "TestCase01GetDayWiseCumulativeMandalDetailsAPITestCase"
]
