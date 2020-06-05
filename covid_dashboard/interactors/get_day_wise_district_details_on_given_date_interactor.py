from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class DistrictStatisticsInteractor:

    def __init__(self, district_storage: DistrictStorageInterface,
                 mandal_storage: MandalStorageInterface,
                 presenter: PresenterInterface):
        self.district_storage = district_storage
        self.mandal_storage = mandal_storage
        self.presenter = presenter

    def get_district_statistics_on_given_date(self, district_id: int,
                                              for_date: str):

        try:
            self.district_storage.is_valid_district_id(district_id)
        except InvalidDistrict:
            self.presenter.raise_exception_for_invalid_district()

        district_statistics_on_date_dto = \
            self.mandal_storage.get_district_statistics_on_given_date(
                for_date=for_date, district_id=district_id
            )

        if type(district_statistics_on_date_dto) is str:
            response = self._make_alternate_response(
                district_statistics_on_date_dto)
        else:
            response = self.presenter\
                       .get_district_statistics_on_given_date_response(
                            district_statistics_on_date_dto=
                            district_statistics_on_date_dto
                        )

        return response

    def _make_alternate_response(self, district_name):
        response = {
            "name": district_name,
            "total_confirmed": 0,
            "total_recovered": 0,
            "total_active": 0,
            "total_deaths": 0,
            "mandals": []
        }
        return response
