from datetime import datetime, date, timedelta
from django.db.models import Sum
from typing import List
from collections import defaultdict

from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.constants.enums import DateFormat
from covid_dashboard.models import DailyStatistics, District, Mandal
from covid_dashboard.interactors.storages.dtos import \
    DistrictActiveCasesDto, DistrictDayWiseStatisticsDto, \
    DistrictsDayWiseCumulativeStatisticsDto, DistrictActiveCasesDto, \
    MandalActiveCasesDto, DistrictCumulativeStatisticsDto, \
    DailyStatisticsDto, DistrictDayWiseCumulativeStatisticsDto, \
    DistrictDailyStatisticsDto
from covid_dashboard.interactors.storages.district_storage_interface import \
    DistrictStorageInterface

class DistrictStorageImplementation(DistrictStorageInterface):
    
    def get_day_wise_districts_cumulative_statistics(self) \
        -> List[DistrictsDayWiseCumulativeStatisticsDto]:

        districts_day_wise_statistics_dtos = \
            self._get_district_wise_statistics_dtos()

        return districts_day_wise_statistics_dtos

    def is_valid_district_id(self, district_id: int):
        try:
            District.objects.get(id=district_id)
        except District.DoesNotExist:
            raise InvalidDistrict

    def get_district_cumulative_statistics(self,
                                           till_date: str,
                                           district_id: int) -> \
        DistrictCumulativeStatisticsDto:

        till_date = self._convert_string_format_date_to_date_object(till_date)

        district_cumulative_statistics_dto = \
            self._get_district_cumulative_statistics_dto(
                till_date=till_date,
                district_id=district_id)

        return district_cumulative_statistics_dto

    def get_day_wise_district_cumulative_statistics(self,
                                                    district_id: int) -> \
        DistrictDayWiseCumulativeStatisticsDto:
        district_day_wise_stats_dicts_list = \
            DailyStatistics.objects.filter(mandal__district_id=district_id)\
                                   .values(
                                       'mandal__district_id',
                                       'mandal__district__name',
                                       'for_date'
                                    ).annotate(
                                        total_confirmed=Sum('total_confirmed'),
                                        total_recovered=Sum('total_recovered'),
                                        total_deaths=Sum('total_deaths')
                                    )
        district_cumulative_statistics_dto = \
            self._get_day_wise_districts_cumulative_data(
                district_day_wise_stats_dicts_list)

        return district_cumulative_statistics_dto

    def _get_day_wise_districts_cumulative_data(self,
            district_day_wise_stats_dicts_list):

        district_name = \
            district_day_wise_stats_dicts_list[0]['mandal__district__name']

        total_district_dicts_list = self._check_date_wise_details(
            district_day_wise_stats_dicts_list)

        district_day_wise_stats_dicts_list = \
            list(district_day_wise_stats_dicts_list)
        district_day_wise_stats_dicts_list += total_district_dicts_list

        district_day_wise_stats_dicts_list = \
            sorted(district_day_wise_stats_dicts_list, key=lambda k:k['for_date'])

        day_wise_statistics_dtos = [
		    self._convert_day_wise_district_dict_to_dto(day_stats)
            for day_stats in district_day_wise_stats_dicts_list
        ]

        return DistrictDayWiseCumulativeStatisticsDto(
            name=district_name,
            date_wise_details=day_wise_statistics_dtos
        )

    def get_day_wise_district_statistics(self, district_id: int) -> \
        List[DistrictDailyStatisticsDto]:
        district_day_wise_dicts_list = \
            DailyStatistics.objects\
                           .filter(mandal__district_id=district_id)\
                           .values(
                               'mandal__district_id',
                               'for_date',
                               'mandal__district__name'
                           ).annotate(
                               total_confirmed=Sum('total_confirmed'),
                               total_recovered=Sum('total_recovered'),
                               total_deaths=Sum('total_deaths')
                           )

        name = district_day_wise_dicts_list[0]['mandal__district__name']
        added_districts_day_wise_dicts_list = \
            self._check_date_wise_details(district_day_wise_dicts_list)

        district_day_wise_dicts_list = list(district_day_wise_dicts_list)
        district_day_wise_dicts_list += added_districts_day_wise_dicts_list

        complete_districts_day_wise_dtos_list = [
            self._convert_daily_district_statistics_dict_dto(
                district_dto, name)
            for district_dto in district_day_wise_dicts_list
        ]

        complete_districts_day_wise_dtos_list = \
            sorted(complete_districts_day_wise_dtos_list,
                   key = lambda k:k.till_date)

        return complete_districts_day_wise_dtos_list

    def _get_day_wise_given_district_statistics(self, district_id):

        district_day_wise_cumulative_dict_list = \
            DailyStatistics.objects\
                           .filter(mandal__district_id=district_id)\
                           .values('mandal__district_id', 'for_date')\
                           .annotate(
                               total_confirmed=Sum('total_confirmed'),
                               total_recovered=Sum('total_recovered'),
                               total_deaths=Sum('total_deaths')
                            )

        name = District.objects.get(id=district_id).name
        district_day_wise_stats_dtos = [
            self._convert_day_wise_district_dict_to_dto(district_details_dict)
            for district_details_dict in 
            district_day_wise_cumulative_dict_list
        ]

        complete_districts_day_wise_dicts_list = \
            DistrictDayWiseCumulativeStatisticsDto(
                name=name,
                date_wise_details=district_day_wise_stats_dtos
            )

        return complete_districts_day_wise_dicts_list
        
    def _get_district_cumulative_statistics_dto(self, till_date, district_id):
        district_cumulative_dict_list = \
            DailyStatistics.objects.filter(
                for_date__lte=till_date,
                mandal__district_id=district_id
            ).values('mandal__district_id')\
             .annotate(
                total_confirmed=Sum('total_confirmed'),
                total_recovered=Sum('total_recovered'),
                total_deaths=Sum('total_deaths')
             )
    
        if not district_cumulative_dict_list.exists():
            district_cumulative_dto = District.objects.get(id=district_id).name
        else:
            district_cumulative_dto = \
                self._convert_district_cumulative_dict_list_to_dto(
                    district_cumulative_dict_list, till_date, district_id
                )

        return district_cumulative_dto

    def _convert_district_cumulative_dict_list_to_dto(self, 
        district_cumulative_dict_list, till_date, district_id):

        district_cumulative_dict = district_cumulative_dict_list[0]
        district = District.objects.get(id=district_id)
        district_cumulative_dict['name'] = district.name
        complete_mandals_cumulative_dicts_list = \
            self._get_mandals_cumulative_dicts_list(till_date, district_id)
        mandal_cumulative_dtos = self._get_mandal_cumulative_dto(
            complete_mandals_cumulative_dicts_list
        )
        district_cumulative_dict['mandals'] = mandal_cumulative_dtos

        district_cumulative_dto = \
            self._convert_district_cumulative_dict_to_dto(
                district_cumulative_dict
            )

        return district_cumulative_dto

    def _get_mandal_cumulative_dto(self, mandals_cumulative_dicts_list):

        mandal_cumulative_dtos = [
            self._convert_mandal_cumulative_dict_to_dto(mandal_dict)
            for mandal_dict in mandals_cumulative_dicts_list
        ]

        return mandal_cumulative_dtos

    def _get_mandals_cumulative_dicts_list(self, till_date, district_id):
        mandals_cumulative_dicts_list = \
            DailyStatistics.objects.filter(for_date__lte=till_date,
                                           mandal__district_id=district_id)\
                                   .values('mandal_id')\
                                   .annotate(
                                       total_confirmed=Sum('total_confirmed'),
                                       total_recovered=Sum('total_recovered'),
                                       total_deaths=Sum('total_deaths')
                                   )
        complete_mandals_cumulative_dicts_list = \
            self._add_name_field_to_mandal_dicts(
                mandals_cumulative_dicts_list, district_id
            )

        return complete_mandals_cumulative_dicts_list

    def _add_name_field_to_mandal_dicts(self,
                                        mandals_cumulative_dict,
                                        district_id):
        mandals = Mandal.objects.filter(district_id=district_id)\
                                .values('id', 'name')

        mandal_names_dict = {}
        for mandal in mandals:
            mandal_names_dict[mandal['id']] = mandal['name']

        mandal_ids_list = [
            mandal_dict['mandal_id']
            for mandal_dict in mandals_cumulative_dict
        ]
        prepared_mandal_dicts = [
            self._make_mandal_cumulative_dict(mandal_id)
            for mandal_id in mandal_names_dict.keys()
            if mandal_id not in mandal_ids_list
        ]
        mandals_cumulative_dict = list(mandals_cumulative_dict)
        mandals_cumulative_dict += prepared_mandal_dicts

        for mandal_dict in mandals_cumulative_dict:
            mandal_id = mandal_dict['mandal_id']
            mandal_dict['name'] = mandal_names_dict[mandal_id]

        return mandals_cumulative_dict

    @staticmethod
    def _make_mandal_cumulative_dict(mandal_id):
        district_dict = {
            "mandal_id": mandal_id,
            "total_confirmed": 0,
            "total_recovered": 0,
            "total_deaths": 0
        }
        return district_dict

    def _get_district_wise_statistics_dtos(self):
        districts_day_wise_statistics_dicts_list = \
            DailyStatistics.objects.values(
                'mandal__district_id',
                'for_date'
            ).annotate(
                total_confirmed=Sum('total_confirmed'),
                total_recovered=Sum('total_recovered'),
                total_deaths=Sum('total_deaths')
            )

        complete_districts_day_wise_dicts_list = \
            self._add_name_field_to_district_dicts(
                districts_day_wise_statistics_dicts_list)

        district_wise_statistics_dict = defaultdict(lambda: [])
        for district_date_stats in complete_districts_day_wise_dicts_list:
            district_id = district_date_stats['mandal__district_id']
            district_wise_statistics_dict[district_id]\
                .append(district_date_stats)

        district_wise_statistics_dtos = \
            self._convert_district_wise_statistics_dict_to_dtos(
                district_wise_statistics_dict=district_wise_statistics_dict
            )

        return district_wise_statistics_dtos

    def _add_name_field_to_district_dicts(self, districts_cumulative_dicts_list):

        districts = District.objects.values('id', 'name')

        districts_names_dict = {}
        for district in districts:
            districts_names_dict[district['id']] = district['name']

        district_ids_list = [
            district_dict['mandal__district_id']
            for district_dict in districts_cumulative_dicts_list
        ]
        prepared_district_dicts = [
            self._make_district_cumulative_dict(district_id)
            for district_id in districts_names_dict.keys()
            if district_id not in district_ids_list
        ]
        districts_cumulative_dicts_list = list(districts_cumulative_dicts_list)
        districts_cumulative_dicts_list += prepared_district_dicts

        for district_dict in districts_cumulative_dicts_list:
            district_id = district_dict['mandal__district_id']
            district_dict['name'] = districts_names_dict[district_id]

        districts_cumulative_dicts_list = \
            sorted(districts_cumulative_dicts_list,
                   key = lambda k:k['mandal__district_id'])

        return districts_cumulative_dicts_list

    @staticmethod
    def _make_district_cumulative_dict(district_id):
        district_dict = {
            "mandal__district_id": district_id,
            "total_confirmed": 0,
            "total_recovered": 0,
            "total_deaths": 0
        }
        return district_dict

    def _convert_district_wise_statistics_dict_to_dtos(self,
        district_wise_statistics_dict):

        district_wise_statistics_dtos = [
            self._convert_statistics_dict_to_dto(district_id, day_wise_stats)
            for district_id, day_wise_stats in
                district_wise_statistics_dict.items()
        ]

        return district_wise_statistics_dtos

    def _convert_statistics_dict_to_dto(self, district_id,
        district_day_wise_stats):

        day_stats = district_day_wise_stats[0]
        district_name = day_stats['name']

        if 'for_date' not in day_stats.keys():
            return DistrictsDayWiseCumulativeStatisticsDto(
                district_id=district_id,
	            name=district_name,
                date_wise_details=[]
            )

        total_district_dicts_list = self._check_date_wise_details(
            district_day_wise_stats)

        district_day_wise_stats = list(district_day_wise_stats)
        district_day_wise_stats += total_district_dicts_list
        district_day_wise_stats = \
            sorted(district_day_wise_stats, key = lambda k:k['for_date'])

        day_wise_statistics_dtos = [
		    self._convert_day_wise_district_dict_to_dto(day_stats)
            for day_stats in district_day_wise_stats
        ]

        district_day_wise_cummulative_dto = \
            DistrictsDayWiseCumulativeStatisticsDto(
                district_id=district_id,
		        name=district_name,
                date_wise_details=day_wise_statistics_dtos
	        )

        return district_day_wise_cummulative_dto

    def _check_date_wise_details(self, district_day_wise_stats):

        total_dicts_list = []
        for_dates = DailyStatistics.objects.values_list(
            'for_date', flat=True)
        for_dates = list(dict.fromkeys(for_dates))

        till_dates_list = [
            district_dict['for_date']
            for district_dict in district_day_wise_stats
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
                    self._make_district_day_wise_statistics_dict(date)
                )

        return total_dicts_list

    def _datetime_range(self, start_date=None, end_date=None):
        span = end_date - start_date
        for i in range(span.days + 1):
            yield start_date + timedelta(days=i)

    def _make_district_day_wise_statistics_dict(self, till_date):
        district_statistics_dict = {
            "for_date": till_date,
            "total_confirmed": 0,
            "total_recovered": 0,
            "total_deaths": 0
        }
        return district_statistics_dict

    @staticmethod
    def _convert_day_wise_district_dict_to_dto(district_details_dict):
        total_active = district_details_dict['total_confirmed'] - (
            district_details_dict['total_deaths'] +
                district_details_dict['total_recovered']
        )

        district_day_wise_statistics_dto = DistrictDayWiseStatisticsDto(
            till_date=district_details_dict['for_date'],
            total_confirmed=district_details_dict['total_confirmed'],
            total_deaths=district_details_dict['total_deaths'],
            total_recovered=district_details_dict['total_recovered'],
            total_active=total_active
        )

        return district_day_wise_statistics_dto

    @staticmethod
    def _convert_district_cumulative_dict_to_dto(district_cumulative_dict):
        total_active = district_cumulative_dict['total_confirmed'] - (
            district_cumulative_dict['total_deaths'] +
                district_cumulative_dict['total_recovered']
        )

        district_cumulative_dto = DistrictCumulativeStatisticsDto(
            name=district_cumulative_dict['name'],
            total_confirmed=district_cumulative_dict['total_confirmed'],
            total_deaths=district_cumulative_dict['total_deaths'],
            total_recovered=district_cumulative_dict['total_recovered'],
            total_active=total_active,
            mandals=district_cumulative_dict['mandals']
        )

        return district_cumulative_dto

    @staticmethod
    def _convert_mandal_cumulative_dict_to_dto(mandal_cumulative_dict):
        total_active = mandal_cumulative_dict['total_confirmed'] - (
            mandal_cumulative_dict['total_deaths'] +
            mandal_cumulative_dict['total_recovered']
        )

        mandal_cumulative_dto = MandalActiveCasesDto(
            mandal_id=mandal_cumulative_dict['mandal_id'],
            name=mandal_cumulative_dict['name'],
            total_confirmed=mandal_cumulative_dict['total_confirmed'],
            total_deaths=mandal_cumulative_dict['total_deaths'],
            total_recovered=mandal_cumulative_dict['total_recovered'],
            total_active=total_active
        )

        return mandal_cumulative_dto

    @staticmethod
    def _convert_daily_district_statistics_dict_dto(district_dto, name):
        district_dto = DistrictDailyStatisticsDto(
            name=name,
            till_date=district_dto['for_date'],
            total_confirmed=district_dto['total_confirmed'],
            total_recovered=district_dto['total_recovered'],
            total_deaths=district_dto['total_deaths']
        )
        return district_dto

    @staticmethod
    def _convert_string_format_date_to_date_object(till_date):

        till_date = datetime.strptime(
            till_date, DateFormat.DATEFORMAT.value
        ).date()

        return till_date
