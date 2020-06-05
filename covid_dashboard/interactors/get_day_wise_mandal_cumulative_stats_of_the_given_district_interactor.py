from datetime import date

from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class MandalsDayWiseCumulativeStatisticsInteractor:
    total_confirmed = 0
    total_deaths = 0
    total_recovered = 0
    total_active = 0

    def __init__(self, district_storage: DistrictStorageInterface,
                 mandal_storage: MandalStorageInterface,
                 presenter: PresenterInterface):
        self.district_storage = district_storage
        self.mandal_storage = mandal_storage
        self.presenter = presenter

    def get_day_wise_mandals_cumulative_statistics_of_the_given_district(
        self, district_id: int):

        try:
            self.district_storage.is_valid_district_id(district_id)
        except InvalidDistrict:
            self.presenter.raise_exception_for_invalid_district()

        day_wise_mandals_statistics_dtos = \
            self.mandal_storage.get_day_wise_mandals_cumulative_statistics(
                district_id=district_id)

        updated_cumulative_statistics_dtos = [
            self._add_day_wise_cumulative_statics(
                mandal_day_wise_stats
            )
            for mandal_day_wise_stats in day_wise_mandals_statistics_dtos
        ]

        response = \
            self.presenter.get_day_wise_mandals_cumulative_statistics_response(
                day_wise_mandals_cumulative_dtos=
                    updated_cumulative_statistics_dtos
            )

        return response

    def _add_day_wise_cumulative_statics(self,
        day_wise_mandal_statistics_dto):

        day_wise_stats = day_wise_mandal_statistics_dto.date_wise_details

        updated_cumulative_statistics = [
            self._add_day_wise_data(mandal_day_stats)
            for mandal_day_stats in day_wise_stats
        ]

        day_wise_mandal_statistics_dto.date_wise_details = \
            updated_cumulative_statistics

        self.total_confirmed = 0
        self.total_deaths = 0
        self.total_recovered = 0
        self.total_active = 0

        return day_wise_mandal_statistics_dto

    def _add_day_wise_data(self, mandal_day_stats):
        mandal_day_stats.total_confirmed += self.total_confirmed
        mandal_day_stats.total_deaths += self.total_deaths
        mandal_day_stats.total_recovered += self.total_recovered
        mandal_day_stats.total_active += self.total_active

        self.total_confirmed = mandal_day_stats.total_confirmed
        self.total_deaths = mandal_day_stats.total_deaths
        self.total_recovered = mandal_day_stats.total_recovered
        self.total_active = mandal_day_stats.total_active

        return mandal_day_stats
