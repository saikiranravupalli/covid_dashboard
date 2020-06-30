# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_day_wise_district_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "districts/{district_id}/day_wise/details/v1/"

from .test_case_01 import TestCase01GetDayWiseDistrictDetailsAPITestCase
from .test_case_02 import TestCase02GetDayWiseDistrictDetailsAPITestCase

__all__ = [
    "TestCase01GetDayWiseDistrictDetailsAPITestCase",
    "TestCase02GetDayWiseDistrictDetailsAPITestCase"
]
