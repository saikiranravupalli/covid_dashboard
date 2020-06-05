# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_districts_day_wise_cumulative_report_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "districts/day_wise/cumulative/v1/"

from .test_case_01 import TestCase01GetDistrictsDayWiseCumulativeReportDetailsAPITestCase

__all__ = [
    "TestCase01GetDistrictsDayWiseCumulativeReportDetailsAPITestCase"
]
