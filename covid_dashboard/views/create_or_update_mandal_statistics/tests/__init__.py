# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "create_or_update_mandal_statistics"
REQUEST_METHOD = "post"
URL_SUFFIX = "districts/{mandal_id}/v1/"

from .test_case_01 import TestCase01CreateOrUpdateMandalStatisticsAPITestCase

__all__ = [
    "TestCase01CreateOrUpdateMandalStatisticsAPITestCase"
]
