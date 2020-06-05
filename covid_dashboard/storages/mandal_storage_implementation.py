from datetime import datetime, timedelta
from django.db.models import Sum
from collections import defaultdict
from typing import List

from covid_dashboard.models import DailyStatistics, Mandal, District
from covid_dashboard.exceptions.exceptions import InvalidMandal, \
    InvalidMandalStatistics
from covid_dashboard.constants.enums import DateFormat
from covid_dashboard.interactors.storages.dtos import \
    DailyStatisticsDto, DistrictOnDateStatisticsDto, MandalStatisticsDto, \
    DistrictOnDateStatisticsDto, MandalsDayWiseCumulativeStatisticsDto, \
    MandalDayWiseStatisticsDto
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

    def get_district_statistics_on_given_date(self,
                                              for_date: str,
                                              district_id: int) -> \
        DistrictOnDateStatisticsDto:

        for_date = self._convert_string_format_date_to_date_object(for_date)

        district_statistics_dto = \
            self._get_state_district_dto(
                for_date=for_date,
                district_id=district_id
            )

        return district_statistics_dto

    def get_day_wise_mandals_cumulative_statistics(self, district_id: int) \
        -> List[MandalsDayWiseCumulativeStatisticsDto]:

        mandals_day_wise_statistics_dtos = \
            self._get_mandals_wise_statistics_dtos_of_the_given_district(
                district_id=district_id)

        return mandals_day_wise_statistics_dtos

    def _get_mandals_wise_statistics_dtos_of_the_given_district(
        self, district_id: int):

        mandals_day_wise_statistics_dicts_list = \
            DailyStatistics.objects.filter(mandal__district_id=district_id)\
                                   .values('mandal_id', 'for_date')\
                                   .annotate(
                                       total_confirmed=Sum('total_confirmed'),
                                       total_recovered=Sum('total_recovered'),
                                       total_deaths=Sum('total_deaths')
                                    )

        complete_mandals_day_wise_dicts_list = \
            self._add_name_field_to_mandals_dicts(
                list(mandals_day_wise_statistics_dicts_list), district_id)

        mandal_wise_statistics_dict = defaultdict(lambda: [])
        for mandal_date_stats in complete_mandals_day_wise_dicts_list:
            mandal_id = mandal_date_stats['mandal_id']
            mandal_wise_statistics_dict[mandal_id]\
                .append(mandal_date_stats)

        district_wise_statistics_dtos = \
            self._convert_mandal_wise_statistics_dict_to_dtos(
                mandal_wise_statistics_dict=mandal_wise_statistics_dict
            )

        return district_wise_statistics_dtos

    def _convert_mandal_wise_statistics_dict_to_dtos(self,
        mandal_wise_statistics_dict):

        mandal_wise_statistics_dtos = [
            self._convert_statistics_dict_to_dto(mandal_id, day_wise_stats)
            for mandal_id, day_wise_stats in
                mandal_wise_statistics_dict.items()
        ]

        return mandal_wise_statistics_dtos

    def _convert_statistics_dict_to_dto(self, mandal_id,
        mandal_day_wise_stats):

        day_stats = mandal_day_wise_stats[0]
        mandal_name = day_stats['name']

        stats = mandal_day_wise_stats[0]
        if 'for_date' not in stats.keys():
            return MandalsDayWiseCumulativeStatisticsDto(
                mandal_id=mandal_id,
		        name=mandal_name,
                date_wise_details=[]
	       )

        total_mandals_dicts_list = self._check_date_wise_details(
            mandal_day_wise_stats)

        mandal_day_wise_stats = list(mandal_day_wise_stats)
        mandal_day_wise_stats += total_mandals_dicts_list
        mandal_day_wise_stats = \
            sorted(mandal_day_wise_stats, key = lambda k:k['for_date'])

        day_wise_statistics_dtos = [
		    self._convert_day_wise_mandal_dict_to_dto(day_stats)
            for day_stats in mandal_day_wise_stats
        ]

        district_day_wise_cummulative_dto = \
            MandalsDayWiseCumulativeStatisticsDto(
                mandal_id=mandal_id,
		        name=mandal_name,
                date_wise_details=day_wise_statistics_dtos
	        )

        return district_day_wise_cummulative_dto

    def _check_date_wise_details(self, mandal_day_wise_stats):

        total_dicts_list = []
        for_dates = DailyStatistics.objects.values_list(
            'for_date', flat=True)
        for_dates = list(dict.fromkeys(for_dates))

        till_dates_list = [
            mandal_dict['for_date']
            for mandal_dict in mandal_day_wise_stats
        ]

        min_till_date = min(for_dates)
        max_till_date = max(for_dates)

        total_dates_list = list(
            self._datetime_range(min_till_date, max_till_date)
        )

        for date in total_dates_list:
            for till_date in till_dates_list:
                if date == till_date:
                    break
            else:
                total_dicts_list.append(
                    self._make_mandal_day_wise_statistics_dict(date)
                )

        return total_dicts_list

    def _datetime_range(self, start_date=None, end_date=None):
        span = end_date - start_date
        for i in range(span.days + 1):
            yield start_date + timedelta(days=i)

    def _make_mandal_day_wise_statistics_dict(self, till_date):
        mandal_statistics_dict = {
            "for_date": till_date,
            "total_confirmed": 0,
            "total_recovered": 0,
            "total_deaths": 0
        }
        return mandal_statistics_dict

    def _get_state_district_dto(self, for_date, district_id):
        district_statistics_dict_list = \
            DailyStatistics.objects.filter(
                for_date=for_date,
                mandal__district_id=district_id
            ).values('mandal__district_id')\
             .annotate(
                 total_confirmed=Sum('total_confirmed'),
                 total_recovered=Sum('total_recovered'),
                 total_deaths=Sum('total_deaths')
            )

        if not district_statistics_dict_list.exists():
            district_statistics_dto = District.objects.get(id=district_id).name
        else:
            district_statistics_dto = \
                self._convert_district_statistics_dict_list_to_dto(
                    district_statistics_dict_list, for_date, district_id
                )

        return district_statistics_dto

    def _convert_district_statistics_dict_list_to_dto(self,
        district_statistics_dict_list, for_date, district_id):

        district_statistics_dict = district_statistics_dict_list[0]

        district = District.objects.get(
            id=district_statistics_dict['mandal__district_id']
        )

        district_statistics_dict['name'] = district.name
        complete_mandals_statistics_dicts_list = \
            self._get_mandals_statistics_dicts_list(for_date, district_id)
        mandal_statistics_dtos = self._get_mandal_statistics_dtos(
            complete_mandals_statistics_dicts_list
        )

        district_statistics_dict['districts'] = mandal_statistics_dtos

        district_statistics_dto = self._convert_district_statistics_dict_to_dto(
            district_statistics_dict)

        return district_statistics_dto

    def _get_mandal_statistics_dtos(self, mandals_statistics_dicts_list):

        mandal_statistics_dtos = [
            self._convert_mandal_statistics_dict_to_dto(mandal_dict)
            for mandal_dict in mandals_statistics_dicts_list
        ]

        return mandal_statistics_dtos

    def _get_mandals_statistics_dicts_list(self, for_date, district_id):

        mandal_statistics_dicts_list = \
            DailyStatistics.objects.filter(
                for_date=for_date,
                mandal__district_id=district_id
            ).values('mandal_id')\
             .annotate(
                 total_confirmed=Sum('total_confirmed'),
                 total_recovered=Sum('total_recovered'),
                 total_deaths=Sum('total_deaths')
            )

        complete_mandal_statistics_dicts_list = \
            self._add_name_field_to_mandals_dicts(
                list(mandal_statistics_dicts_list), district_id
            )

        return complete_mandal_statistics_dicts_list

    def _add_name_field_to_mandals_dicts(self,
                                         mandal_statistics_dicts_list,
                                         district_id):
        mandals = Mandal.objects.filter(district_id=district_id)\
                                .values('id', 'name')
        mandal_names_dict = {}
        for mandal in mandals:
            mandal_names_dict[mandal['id']] = mandal['name']

        mandal_ids_list = [
            mandal_dict['mandal_id']
            for mandal_dict in mandal_statistics_dicts_list
        ]
        prepared_mandal_dicts = [
            self._make_mandal_statistics_dict(mandal_id)
            for mandal_id in mandal_names_dict.keys()
            if mandal_id not in mandal_ids_list
        ]
        mandal_statistics_dicts_list += prepared_mandal_dicts

        for mandal_dict in mandal_statistics_dicts_list:
            mandal_id = mandal_dict['mandal_id']
            mandal_dict['name'] = mandal_names_dict[mandal_id]

        mandal_statistics_dicts_list = \
            sorted(mandal_statistics_dicts_list,
                   key = lambda k:k['mandal_id'])

        return mandal_statistics_dicts_list

    @staticmethod
    def _make_mandal_statistics_dict(mandal_id):
        district_dict = {
            "mandal_id": mandal_id,
            "total_confirmed": 0,
            "total_recovered": 0,
            "total_deaths": 0
        }
        return district_dict

    @staticmethod
    def _convert_district_statistics_dict_to_dto(district_statistics_dict):

        district_statistics_dto = DistrictOnDateStatisticsDto(
            name=district_statistics_dict['name'],
            total_confirmed=district_statistics_dict['total_confirmed'],
            total_deaths=district_statistics_dict['total_deaths'],
            total_recovered=district_statistics_dict['total_recovered'],
            mandals=district_statistics_dict['districts']
        )

        return district_statistics_dto

    @staticmethod
    def _convert_mandal_statistics_dict_to_dto(mandal_statistics_dict):

        mandal_statistics_dto = MandalStatisticsDto(
            mandal_id=mandal_statistics_dict['mandal_id'],
            name=mandal_statistics_dict['name'],
            total_confirmed=mandal_statistics_dict['total_confirmed'],
            total_deaths=mandal_statistics_dict['total_deaths'],
            total_recovered=mandal_statistics_dict['total_recovered']
        )

        return mandal_statistics_dto

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

    @staticmethod
    def _convert_day_wise_mandal_dict_to_dto(mandal_details_dict):
        total_active = mandal_details_dict['total_confirmed'] - (
            mandal_details_dict['total_deaths'] +
                mandal_details_dict['total_recovered']
        )

        district_day_wise_statistics_dto = MandalDayWiseStatisticsDto(
            till_date=mandal_details_dict['for_date'],
            total_confirmed=mandal_details_dict['total_confirmed'],
            total_deaths=mandal_details_dict['total_deaths'],
            total_recovered=mandal_details_dict['total_recovered'],
            total_active=total_active
        )

        return district_day_wise_statistics_dto

    @staticmethod
    def _convert_string_format_date_to_date_object(till_date):

        till_date = datetime.strptime(
            till_date, DateFormat.DATEFORMAT.value
        ).date()

        return till_date    
