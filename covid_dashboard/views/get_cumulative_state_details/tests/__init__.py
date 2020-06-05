# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_cumulative_state_details"
REQUEST_METHOD = "post"
URL_SUFFIX = "state/cumulative/v1/"

from .test_case_01 import TestCase01GetCumulativeStateDetailsAPITestCase

__all__ = [
    "TestCase01GetCumulativeStateDetailsAPITestCase"
]
