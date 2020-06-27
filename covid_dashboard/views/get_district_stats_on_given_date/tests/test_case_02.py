"""
# TODO: get_district_stats_on_given_date with valid district_id returns value
"""

from covid_dashboard.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "for_date": "3/6/2020"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"district_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://localhost:8080/o/token", "flow": "password", "scopes": ["read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02GetDistrictStatsOnGivenDateAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02GetDistrictStatsOnGivenDateAPITestCase, self).\
            setupUser(username=username, password=password)

        self.statistics()


    def test_case(self):
        response = self.default_test_case()
        import json

        response_content = json.loads(response.content)

        self.assert_match_snapshot(
            name='get_district_stats_on_given_date_response',
            value=response_content
        )