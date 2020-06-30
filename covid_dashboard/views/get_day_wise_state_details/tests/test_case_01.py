"""
# TODO: get_day_wise_state_details
"""

from covid_dashboard.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://localhost:8080/o/token", "flow": "password", "scopes": ["read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetDayWiseStateDetailsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    
    def setupUser(self, username, password):
        super(TestCase01GetDayWiseStateDetailsAPITestCase, self).setupUser(
            username=username, password=password
        )

        self.statistics()

    def test_case(self):
        response = self.default_test_case()
        import json

        response_content = json.loads(response.content)

        self.assert_match_snapshot(
            name='get_day_wise_state_details_response',
            value=response_content
        )
