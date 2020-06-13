from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class DistrictDayWiseCumulativeStatisticsInteractor:
    total_confirmed = 0
    total_deaths = 0
    total_recovered = 0
    total_active = 0

    def __init__(self, storage: DistrictStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_district_cumulative_statistics(self, district_id: int):

        try:
            self.storage.is_valid_district_id(district_id)
        except InvalidDistrict:
            self.presenter.raise_exception_for_invalid_district()

        day_wise_district_cumulative_statistics_dto = \
            self.storage.get_day_wise_district_cumulative_statistics(
                district_id=district_id)

        if day_wise_district_cumulative_statistics_dto is None:
            return []

        updated_cumulative_statistics_dto = \
            self._add_day_wise_cumulative_statics(
                day_wise_district_cumulative_statistics_dto.date_wise_details
            )

        day_wise_district_cumulative_statistics_dto.date_wise_details = \
            updated_cumulative_statistics_dto

        response = \
            self.presenter.get_day_wise_district_cumulative_statistics_response(
                day_wise_district_cumulative_dto=
                    day_wise_district_cumulative_statistics_dto
            )

        return response

    def _add_day_wise_cumulative_statics(self, day_wise_district_statistics_dtos):

        updated_cumulative_statistics = [
            self._add_cumulative_data(district)
            for district in day_wise_district_statistics_dtos
        ]

        return updated_cumulative_statistics

    def _add_cumulative_data(self, district_dto):
        district_dto.total_confirmed += self.total_confirmed
        district_dto.total_deaths += self.total_deaths
        district_dto.total_recovered += self.total_recovered
        district_dto.total_active += self.total_active

        self.total_confirmed = district_dto.total_confirmed
        self.total_deaths = district_dto.total_deaths
        self.total_recovered = district_dto.total_recovered
        self.total_active = district_dto.total_active

        return district_dto
