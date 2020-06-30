# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_cumulative_district_details"
REQUEST_METHOD = "post"
URL_SUFFIX = "districts/{district_id}/cumulative/v1/"

from .test_case_01 import TestCase01GetCumulativeDistrictDetailsAPITestCase
from .test_case_02 import TestCase02GetCumulativeDistrictDetailsAPITestCase

__all__ = [
    "TestCase01GetCumulativeDistrictDetailsAPITestCase",
    "TestCase02GetCumulativeDistrictDetailsAPITestCase"
]
