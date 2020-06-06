# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_district_wise_zone_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "districts/zones/v1/"

from .test_case_01 import TestCase01GetDistrictWiseZoneDetailsAPITestCase

__all__ = [
    "TestCase01GetDistrictWiseZoneDetailsAPITestCase"
]
