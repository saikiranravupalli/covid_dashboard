# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_day_wise_state_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/day_wise/details/v1/"

from .test_case_01 import TestCase01GetDayWiseStateDetailsAPITestCase

__all__ = [
    "TestCase01GetDayWiseStateDetailsAPITestCase"
]
