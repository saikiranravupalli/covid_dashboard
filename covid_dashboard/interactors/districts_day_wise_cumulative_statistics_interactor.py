from datetime import date
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class DistrictsDayWiseCumulativeStatisticsInteractor:
    total_confirmed = 0
    total_deaths = 0
    total_recovered = 0
    total_active = 0

    def __init__(self, storage: DistrictStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_districts_cumulative_statistics(self):

        day_wise_districts_statistics_dtos = \
            self.storage.get_day_wise_districts_cumulative_statistics()

        updated_cumulative_statistics_dtos = [
            self._add_day_wise_cumulative_statics(district_day_wise_stats)
            for district_day_wise_stats in day_wise_districts_statistics_dtos
        ]

        response = \
            self.presenter.get_day_wise_districts_cumulative_statistics_response(
                day_wise_districts_cumulative_dtos=
                updated_cumulative_statistics_dtos
            )

        return response

    def _add_day_wise_cumulative_statics(self,
        day_wise_district_statistics_dto):

        day_wise_stats = day_wise_district_statistics_dto.date_wise_details

        updated_cumulative_statistics = [
            self._add_day_wise_data(district_day_stats)
            for district_day_stats in day_wise_stats
        ]

        day_wise_district_statistics_dto.date_wise_details = \
            updated_cumulative_statistics

        self.total_confirmed = 0
        self.total_deaths = 0
        self.total_recovered = 0
        self.total_active = 0

        return day_wise_district_statistics_dto

    def _add_day_wise_data(self, district_day_stats):
        district_day_stats.total_confirmed += self.total_confirmed
        district_day_stats.total_deaths += self.total_deaths
        district_day_stats.total_recovered += self.total_recovered
        district_day_stats.total_active += self.total_active

        self.total_confirmed = district_day_stats.total_confirmed
        self.total_deaths = district_day_stats.total_deaths
        self.total_recovered = district_day_stats.total_recovered
        self.total_active = district_day_stats.total_active

        return district_day_stats
