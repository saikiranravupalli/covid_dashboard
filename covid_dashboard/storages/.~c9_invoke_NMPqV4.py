from typing import List

from covid_dashboard.models import DailyStatistics
from covid_dashboard.interactors.storages.dtos import \
    DailyStatisticsDto
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface

class MandalStorageImplementation(MandalStorageInterface):

    def is_valid_mandal_id(self, mandal_id: int):
        try:
            Mandal.objects.get(id=mandal_id)
        except Mandal.DoesNotExist:
            raise InvalidMandal

    def is_mandal_stats_exists(self, for_date: str, mandal_id: int):
 
        for_date = self._convert_string_format_date_to_date_object(for_date)

        try:
            DailyStatistics.objects.get(for_date=for_date,
                                        mandal_id=mandal_id)
        except DailyStatistics.DoesNotExist:
            raise InvalidMandalStatistics

    def update_mandal_statistics(self,
                                 for_date: int,
                                 total_confirmed: int,
                                 total_recovered: int,
                                 total_deaths: int,
                                 mandal_id: int):

        for_date = self._convert_string_format_date_to_date_object(for_date)

        statistics_list = DailyStatistics.objects.filter(for_date=for_date,
                                                         mandal_id=mandal_id)
        statistics = statistics_list[0]
        statistics.total_confirmed = total_confirmed
        statistics.total_deaths = total_deaths
        statistics.total_recovered = total_recovered
        statistics.save()

    def create_mandal_statistics(self,
                                 for_date: int,
                                 total_confirmed: int,
                                 total_recovered: int,
                                 total_deaths: int,
                                 mandal_id: int):

        for_date = self._convert_string_format_date_to_date_object(for_date)

        DailyStatistics.objects.create(
            for_date=for_date,
            total_confirmed=total_confirmed,
            total_deaths=total_deaths,
            total_recovered=total_recovered,
            mandal_id=mandal_id
        )

    def get_daily_statistics(self) -> List[DailyStatisticsDto]:
        daily_statistics_dicts_list = \
            DailyStatistics.objects.values('for_date',
                                           'mandal__district_id',
                                           'mandal__district__name',
                                           'mandal__name',
                                           'mandal_id',
                                           'total_confirmed',
                                           'total_deaths',
                                           'total_recovered')

        daily_statistics_dtos = [
            self._convert_daily_statistics_dict_to_dto(
                daily_statistics=daily_statistics
            )
            for daily_statistics in daily_statistics_dicts_list
        ]
        return daily_statistics_dtos

    @staticmethod
    def _convert_daily_statistics_dict_to_dto(daily_statistics):
        daily_statistics_dto = DailyStatisticsDto(
            for_date = daily_statistics['for_date'],
            district_id=daily_statistics['mandal__district_id'],
            district_name=daily_statistics['mandal__district__name'],
            mandal_id=daily_statistics['mandal_id'],
            mandal_name=daily_statistics['mandal__name'],
            total_confirmed=daily_statistics['total_confirmed'],
            total_deaths=daily_statistics['total_recovered'],
            total_recovered=daily_statistics['total_deaths']
        )
        return daily_statistics_dto
