from datetime import datetime, date, timedelta
from django.db.models import Sum
from typing import List
from collections import defaultdict

from covid_dashboard.exceptions.exceptions import InvalidMandalStatistics, \
    InvalidMandal, InvalidDistrict
from covid_dashboard.constants.enums import DateFormat
from covid_dashboard.models import DailyStatistics, State, District
from covid_dashboard.interactors.storages.dtos import \
    StateCumulativeStatisticsDto, DistrictActiveCasesDto, \
    StateDayWiseCumulativeStatisticsDto, DistrictActiveCasesDto, \
    StateStatisticsDto, DistrictStatisticsDto, StateDayWiseStatisticsDto
from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface


class StateStorageImplementation(StateStorageInterface):

    def get_state_cumulative_statistics(self, till_date: str) \
        -> StateCumulativeStatisticsDto:

        for_date = self._convert_string_format_date_to_date_object(till_date)

        state_cumulative_statistics_dto = \
            self._get_state_cumulative_dto(for_date=for_date)

        return state_cumulative_statistics_dto

    def get_day_wise_state_cumulative_statistics(self) \
        -> List[StateDayWiseCumulativeStatisticsDto]:

        state_day_wise_statistics_dicts_list = \
            self._get_state_day_wise_statistics_dto()
    
        state_day_wise_statistics_dtos = \
            self._convert_statistics_list_to_dtos_with_active_cases(
                state_day_wise_statistics_dicts_list
            )

        return state_day_wise_statistics_dtos

    def get_state_statistics_on_given_date(self, for_date: str) -> \
        StateStatisticsDto:
        for_date = self._convert_string_format_date_to_date_object(for_date)

        state_statistics_dto = \
            self._get_state_statistics_dto(for_date=for_date)

        return state_statistics_dto

    def get_day_wise_state_statistics(self) -> \
        List[StateDayWiseStatisticsDto]:

        state_day_wise_statistics_dicts_list = \
            self._get_state_day_wise_statistics_dto()
    
        state_day_wise_statistics_dtos = \
            self._convert_statistics_list_to_dtos(
                state_day_wise_statistics_dicts_list
            )

        return state_day_wise_statistics_dtos

    def _convert_statistics_list_to_dtos(self,
        state_day_wise_statistics_list):

        state_day_wise_statistics_dtos = [
            self._convert_day_wise_state_dict_to_dto(
                state_details_dict
            )
            for state_details_dict in state_day_wise_statistics_list
        ]

        return state_day_wise_statistics_dtos

    def _get_state_statistics_dto(self, for_date):

        state_statistics_dict_list = \
            DailyStatistics.objects.filter(for_date=for_date)\
                                   .values('mandal__district__state_id')\
                                   .annotate(
                                       total_confirmed=Sum('total_confirmed'),
                                       total_recovered=Sum('total_recovered'),
                                       total_deaths=Sum('total_deaths')
                                    )

        if not state_statistics_dict_list.exists():
            state_statistics_dto = None
        else:
            state_statistics_dto = \
                self._convert_state_statistics_dict_list_to_dto(
                    state_statistics_dict_list, for_date
                )

        return state_statistics_dto

    def _convert_state_statistics_dict_list_to_dto(self,
        state_statistics_dict_list, for_date):

        state_statistics_dict = state_statistics_dict_list[0]

        state = State.objects.get(
            id=state_statistics_dict['mandal__district__state_id']
        )

        state_statistics_dict['name'] = state.name
        complete_districts_statistics_dicts_list = \
            self._get_district_statistics_dicts_list(for_date)
        district_statistics_dtos = self._get_district_statistics_dtos(
            complete_districts_statistics_dicts_list
        )

        state_statistics_dict['districts'] = district_statistics_dtos

        state_statistics_dto = self._convert_state_statistics_dict_to_dto(
            state_statistics_dict)

        return state_statistics_dto

    def _get_district_statistics_dicts_list(self, for_date):

        districts_statistics_dicts_list = \
            DailyStatistics.objects.filter(for_date=for_date)\
                                   .values('mandal__district_id')\
                                   .annotate(
                                       total_confirmed=Sum('total_confirmed'),
                                       total_recovered=Sum('total_recovered'),
                                       total_deaths=Sum('total_deaths')
                                    )

        complete_districts_statistics_dicts_list = \
            self._add_name_field_to_district_dicts(
                list(districts_statistics_dicts_list)
            )

        return complete_districts_statistics_dicts_list

    def _get_district_statistics_dtos(self, districts_statistics_dicts_list):

        district_statistics_dtos = [
            self._convert_district_statistics_dict_to_dto(district_dict)
            for district_dict in districts_statistics_dicts_list
        ]

        return district_statistics_dtos

    def _get_state_day_wise_statistics_dto(self):

        state_day_wise_statistics_list = \
            DailyStatistics.objects.values(
                'for_date',
                'mandal__district__state_id'
            ).annotate(
                total_confirmed=Sum('total_confirmed'),
                total_recovered=Sum('total_recovered'),
                total_deaths=Sum('total_deaths')
            )

        updated_state_day_wise_statistics_list = \
            self._add_name_field_to_state_dicts(
                state_day_wise_statistics_list
            )

        return updated_state_day_wise_statistics_list

    def _convert_statistics_list_to_dtos_with_active_cases(self,
        state_day_wise_statistics_list):

        state_day_wise_statistics_dtos = [
            self._convert_day_wise_state_dict_to_dto_with_active_cases(
                state_details_dict
            )
            for state_details_dict in state_day_wise_statistics_list
        ]

        return state_day_wise_statistics_dtos

    def _add_name_field_to_state_dicts(self, state_day_wise_statistics_list):
        state_day_wise_statistics_dict = state_day_wise_statistics_list[0]
        state = State.objects.get(
            id=state_day_wise_statistics_dict['mandal__district__state_id']
        )
        state_name = state.name

        till_dates_list = [
            state_dict['for_date']
            for state_dict in state_day_wise_statistics_list
        ]
        min_till_date = min(till_dates_list)
        max_till_date = max(till_dates_list)

        total_dates_list = list(
            self._datetime_range(min_till_date, max_till_date)
        )

        total_dicts_list = []
        for date in total_dates_list:
            for till_date in till_dates_list:
                if date == till_date:
                    break
            else:
                total_dicts_list.append(
                    self._make_state_day_wise_statistics_dict(date)
                )

        state_day_wise_statistics_list = list(state_day_wise_statistics_list)
        state_day_wise_statistics_list += total_dicts_list

        for state_day_stats in state_day_wise_statistics_list:
            state_day_stats['name'] = state_name

        state_day_wise_statistics_list = \
            sorted(state_day_wise_statistics_list, key = lambda k:k['for_date'])

        return state_day_wise_statistics_list

    def _make_state_day_wise_statistics_dict(self, till_date):
        state_statistics_dict = {
            "for_date": till_date,
            "mandal__district__state_id": 1,
            "total_confirmed": 0,
            "total_recovered": 0,
            "total_deaths": 0
        }
        return state_statistics_dict

    def _datetime_range(self, start_date=None, end_date=None):
        span = end_date - start_date
        for i in range(span.days + 1):
            yield start_date + timedelta(days=i)

    def _get_state_cumulative_dto(self, for_date):

        state_cumulative_dict_list = \
            DailyStatistics.objects.filter(for_date__lte=for_date)\
                                   .values('mandal__district__state_id')\
                                   .annotate(
                                       total_confirmed=Sum('total_confirmed'),
                                       total_recovered=Sum('total_recovered'),
                                       total_deaths=Sum('total_deaths')
                                    )

        if not state_cumulative_dict_list.exists():
            state_cumulative_dto = None
        else:
            state_cumulative_dto = \
                self._convert_state_cumulative_dict_list_to_dto(
                    state_cumulative_dict_list, for_date
                )

        return state_cumulative_dto

    def _convert_state_cumulative_dict_list_to_dto(self,
        state_cumulative_dict_list, for_date):

        state_cumulative_dict = state_cumulative_dict_list[0]

        state = State.objects.get(
            id=state_cumulative_dict['mandal__district__state_id']
        )

        state_cumulative_dict['name'] = state.name
        complete_districts_cumulative_dicts_list = \
            self._get_district_cumulative_dicts_list(for_date)
        district_cumulative_dtos = self._get_district_cumulative_dto(
            complete_districts_cumulative_dicts_list
        )

        state_cumulative_dict['districts'] = district_cumulative_dtos

        state_cumulative_dto = self._convert_state_cumulative_dict_to_dto(
            state_cumulative_dict)

        return state_cumulative_dto

    def _get_district_cumulative_dicts_list(self, for_date):

        districts_cumulative_dicts_list = \
            DailyStatistics.objects.filter(for_date__lte=for_date)\
                                   .values('mandal__district_id')\
                                   .annotate(
                                       total_confirmed=Sum('total_confirmed'),
                                       total_recovered=Sum('total_recovered'),
                                       total_deaths=Sum('total_deaths')
                                    )

        complete_districts_cumulative_dicts_list = \
            self._add_name_field_to_district_dicts(
                list(districts_cumulative_dicts_list)
            )

        return complete_districts_cumulative_dicts_list

    def _get_district_cumulative_dto(self, districts_cumulative_dicts_list):

        district_cumulative_dtos = [
            self._convert_districts_cumulative_dict_to_dto(district_dict)
            for district_dict in districts_cumulative_dicts_list
        ]

        return district_cumulative_dtos

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

    @staticmethod
    def _convert_day_wise_state_dict_to_dto_with_active_cases(state_details_dict):
        total_active = state_details_dict['total_confirmed'] - (
            state_details_dict['total_deaths'] +
                state_details_dict['total_recovered']
        )

        state_day_wise_statistics_dto = StateDayWiseCumulativeStatisticsDto(
            name=state_details_dict['name'],
            till_date=state_details_dict['for_date'],
            total_confirmed=state_details_dict['total_confirmed'],
            total_deaths=state_details_dict['total_deaths'],
            total_recovered=state_details_dict['total_recovered'],
            total_active=total_active
        )

        return state_day_wise_statistics_dto

    @staticmethod
    def _convert_districts_cumulative_dict_to_dto(district_cumulative_dict):

        total_active = district_cumulative_dict['total_confirmed'] - (
            district_cumulative_dict['total_deaths'] +
            district_cumulative_dict['total_recovered']
        )

        district_cumulative_dto = DistrictActiveCasesDto(
            district_id=district_cumulative_dict['mandal__district_id'],
            name=district_cumulative_dict['name'],
            total_confirmed=district_cumulative_dict['total_confirmed'],
            total_deaths=district_cumulative_dict['total_deaths'],
            total_recovered=district_cumulative_dict['total_recovered'],
            total_active=total_active
        )

        return district_cumulative_dto

    @staticmethod
    def _convert_state_cumulative_dict_to_dto(state_cumulative_dict):

        total_active = state_cumulative_dict['total_confirmed'] - (
            state_cumulative_dict['total_deaths'] +
                state_cumulative_dict['total_recovered']
        )

        state_cumulative_dto = StateCumulativeStatisticsDto(
            name=state_cumulative_dict['name'],
            total_confirmed=state_cumulative_dict['total_confirmed'],
            total_deaths=state_cumulative_dict['total_deaths'],
            total_recovered=state_cumulative_dict['total_recovered'],
            total_active=total_active,
            districts=state_cumulative_dict['districts']
        )

        return state_cumulative_dto

    @staticmethod
    def _convert_state_statistics_dict_to_dto(state_statistics_dict):

        state_cumulative_dto = StateStatisticsDto(
            name=state_statistics_dict['name'],
            total_confirmed=state_statistics_dict['total_confirmed'],
            total_deaths=state_statistics_dict['total_deaths'],
            total_recovered=state_statistics_dict['total_recovered'],
            districts=state_statistics_dict['districts']
        )

        return state_cumulative_dto

    @staticmethod
    def _convert_district_statistics_dict_to_dto(district_statistics_dict):

        district_statistics_dto = DistrictStatisticsDto(
            district_id=district_statistics_dict['mandal__district_id'],
            name=district_statistics_dict['name'],
            total_confirmed=district_statistics_dict['total_confirmed'],
            total_deaths=district_statistics_dict['total_deaths'],
            total_recovered=district_statistics_dict['total_recovered']
        )

        return district_statistics_dto

    @staticmethod
    def _convert_day_wise_state_dict_to_dto(state_details_dict):
        state_day_wise_statistics_dto = StateDayWiseStatisticsDto(
            name=state_details_dict['name'],
            till_date=state_details_dict['for_date'],
            total_confirmed=state_details_dict['total_confirmed'],
            total_deaths=state_details_dict['total_deaths'],
            total_recovered=state_details_dict['total_recovered']
        )

        return state_day_wise_statistics_dto

    @staticmethod
    def _convert_string_format_date_to_date_object(till_date):

        till_date = datetime.strptime(
            till_date, DateFormat.DATEFORMAT.value
        ).date()

        return till_date
