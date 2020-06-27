"""
# TODO: Update or create mandal statistics with valid details updates daily statistics
"""

from datetime import date
from covid_dashboard.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from covid_dashboard.factories.factories import DailyStatisticsFactory
from covid_dashboard.models import DailyStatistics
from covid_dashboard.constants.enums import DateFormat

REQUEST_BODY = """
{
    "for_date": "1/6/2020",
    "total_confirmed": 1,
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


class TestCase05CreateOrUpdateMandalStatisticsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase05CreateOrUpdateMandalStatisticsAPITestCase, self).\
            setupUser(username=username, password=password)

        self.foo_user.is_admin = True
        self.foo_user.save()

        DailyStatisticsFactory(for_date=date(2020, 6, 1))

    def test_case(self):
        self.default_test_case()

        mandal_id = TEST_CASE['request']['path_params']['mandal_id']

        daily_statistics = DailyStatistics.objects.get(mandal_id=mandal_id)

        self.assert_match_snapshot(
            name='mandal_id',
            value=daily_statistics.mandal_id
        )
        self.assert_match_snapshot(
            name='for_date',
            value=daily_statistics.for_date.strftime(
                DateFormat.DATEFORMAT.value
            )
        )
        self.assert_match_snapshot(
            name='total_confirmed',
            value=daily_statistics.total_confirmed
        )
        self.assert_match_snapshot(
            name='total_recovered',
            value=daily_statistics.total_recovered
        )
        self.assert_match_snapshot(
            name='total_deaths',
            value=daily_statistics.total_deaths
        )
        