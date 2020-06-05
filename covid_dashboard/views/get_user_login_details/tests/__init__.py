# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_user_login_details"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01GetUserLoginDetailsAPITestCase

__all__ = [
    "TestCase01GetUserLoginDetailsAPITestCase"
]
