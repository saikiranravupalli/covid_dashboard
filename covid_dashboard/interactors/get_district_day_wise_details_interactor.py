from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.dtos import \
    StateDayWiseStatisticsDto

class DistrictDayWiseStatisticsInteractor:

    def __init__(self, storage: DistrictStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_district_statistics(self, district_id: int):

        try:
            self.storage.is_valid_district_id(district_id)
        except InvalidDistrict:
            self.presenter.raise_exception_for_invalid_district()

        day_wise_district_statistics_dtos = \
            self.storage.get_day_wise_district_statistics(
                district_id=district_id)

        if day_wise_district_statistics_dtos is None:
            return []

        response = \
            self.presenter.get_day_wise_district_statistics_response(
                day_wise_district_statistics_dtos=day_wise_district_statistics_dtos
            )

        return response
