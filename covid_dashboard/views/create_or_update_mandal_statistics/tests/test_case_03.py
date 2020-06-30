"""
# TODO: Update or create mandal statistics with invalid values raises error
"""

from covid_dashboard.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from covid_dashboard.factories.factories import MandalFactory

REQUEST_BODY = """
{
    "for_date": "5/2/2020",
    "total_confirmed": -1,
    "total_deaths": 1,
    "total_recovered": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"mandal_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {
            "oauth": {
                "tokenUrl": "http://localhost:8080/o/token",
                "flow": "password",
                "scopes": ["write"],
                "type": "oauth2"
            }
        },
        "body": REQUEST_BODY,
    },
}


class TestCase03CreateOrUpdateMandalStatisticsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase03CreateOrUpdateMandalStatisticsAPITestCase, self).\
            setupUser(username=username, password=password)

        self.foo_user.is_admin = True
        self.foo_user.save()
        MandalFactory()

    def test_case(self):
        self.default_test_case()