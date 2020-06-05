from datetime import date

from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class DistrictCumulativeStatisticsInteractor:

    def __init__(self, storage: DistrictStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_district_cumulative_statistics(self,
                                           till_date: str,
                                           district_id: int):

        try:
            self.storage.is_valid_district_id(district_id)
        except InvalidDistrict:
            self.presenter.raise_exception_for_invalid_district()

        district_cumulative_statistics_dto = \
            self.storage.get_district_cumulative_statistics(
                till_date=till_date, district_id=district_id
            )

        if type(district_cumulative_statistics_dto) is str:
            response = self._make_alternate_response(
                district_cumulative_statistics_dto)
        else:
            response = \
                self.presenter.get_district_cumulative_statistics_response(
                    district_cumulative_statistics_dto=
                    district_cumulative_statistics_dto
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
