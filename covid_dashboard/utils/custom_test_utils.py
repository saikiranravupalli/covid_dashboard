from django_swagger_utils.utils.test import CustomAPITestCase

from covid_dashboard.factories.factories import StateFactory, \
    DistrictFactory, MandalFactory, DailyStatisticsFactory

class CustomTestUtils(CustomAPITestCase):

    def setupUser(self, username, password):
        super(CustomTestUtils, self).setupUser(
            username=username, password=password
        )

        StateFactory.reset_sequence()
        DistrictFactory.reset_sequence()
        MandalFactory.reset_sequence()
        DailyStatisticsFactory.reset_sequence()

    def statistics(self):
        state = StateFactory()
        districts = DistrictFactory.create_batch(5, state=state)

        mandals = []
        for district in districts:
            mandals += MandalFactory.create_batch(2, district=district)

        for mandal in mandals:
            DailyStatisticsFactory.create_batch(5, mandal=mandal)
