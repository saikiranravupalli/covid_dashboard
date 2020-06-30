# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "create_or_update_mandal_statistics"
REQUEST_METHOD = "post"
URL_SUFFIX = "districts/{mandal_id}/v1/"

from .test_case_01 import TestCase01CreateOrUpdateMandalStatisticsAPITestCase
from .test_case_02 import TestCase02CreateOrUpdateMandalStatisticsAPITestCase
from .test_case_03 import TestCase03CreateOrUpdateMandalStatisticsAPITestCase
from .test_case_04 import TestCase04CreateOrUpdateMandalStatisticsAPITestCase
from .test_case_05 import TestCase05CreateOrUpdateMandalStatisticsAPITestCase

__all__ = [
    "TestCase01CreateOrUpdateMandalStatisticsAPITestCase",
    "TestCase02CreateOrUpdateMandalStatisticsAPITestCase",
    "TestCase03CreateOrUpdateMandalStatisticsAPITestCase",
    "TestCase04CreateOrUpdateMandalStatisticsAPITestCase",
    "TestCase05CreateOrUpdateMandalStatisticsAPITestCase"
]
