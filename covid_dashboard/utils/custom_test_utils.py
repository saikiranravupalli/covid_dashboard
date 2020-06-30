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

        mandals_list = []
        for district in districts:
            mandals_list += MandalFactory.create_batch(2, district=district)

        for mandal in mandals_list:
            DailyStatisticsFactory.create_batch(5, mandal=mandal)
