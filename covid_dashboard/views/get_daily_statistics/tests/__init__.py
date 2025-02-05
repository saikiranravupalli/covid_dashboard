# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_daily_statistics"
REQUEST_METHOD = "get"
URL_SUFFIX = "statistics/admin/v1/"

from .test_case_01 import TestCase01GetDailyStatisticsAPITestCase
from .test_case_02 import TestCase02GetDailyStatisticsAPITestCase

__all__ = [
    "TestCase01GetDailyStatisticsAPITestCase",
    "TestCase02GetDailyStatisticsAPITestCase"
]
