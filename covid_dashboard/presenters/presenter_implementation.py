import pytest
from typing import List
from django_swagger_utils.drf_server.exceptions import BadRequest, Forbidden
from covid_dashboard.exceptions.exception_messages import INVALID_MANDAL_ID, \
    INVALID_POSITIVE_NUMBER, INVALID_ACCESS, INVALID_DISTRICT_ID

from covid_dashboard.constants.enums import DistrictZones, DateFormat
from covid_dashboard.interactors.storages.dtos import \
    StateCumulativeStatisticsDto, DistrictActiveCasesDto, \
    StateDayWiseCumulativeStatisticsDto, StateStatisticsDto, \
    DistrictsDayWiseCumulativeStatisticsDto, DistrictCumulativeStatisticsDto,\
    MandalActiveCasesDto, StateDayWiseStatisticsDto, DailyStatisticsDto, \
    DistrictDayWiseCumulativeStatisticsDto, DistrictOnDateStatisticsDto, \
    MandalStatisticsDto, MandalsDayWiseCumulativeStatisticsDto, \
    DistrictDailyStatisticsDto, DistrictZonesDto
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_user_admin(self):
        raise Forbidden(*INVALID_ACCESS)

    def get_state_cumulative_statistics_response(self,
        state_cumulative_statistics_dto: StateCumulativeStatisticsDto):

        district_cumulative_dicts_list = [
            self._convert_district_cumulative_statistics_dtos_to_dict(
                district_dto=district_dto)
            for district_dto in state_cumulative_statistics_dto.districts
        ]

        response = self._convert_state_cumulative_statistics_dto_to_dict(
            state_cumulative_statistics_dto=state_cumulative_statistics_dto,
            district_cumulative_dicts_list=district_cumulative_dicts_list
        )

        return response

    def get_day_wise_state_cumulative_statistics_response(self,
        day_wise_state_cumulative_dtos:
            List[StateDayWiseCumulativeStatisticsDto]):

        state_dto = day_wise_state_cumulative_dtos[0]
        state_name = state_dto.name
        cumulative_day_wise_dict_list = [
            self._convert_day_wise_cumulative_statistics_dict_to_dto(
                day_wise_dto)
            for day_wise_dto in day_wise_state_cumulative_dtos
        ]

        response = {
            "name": state_name,
            "date_wise_details": cumulative_day_wise_dict_list
        }

        return response

    def get_day_wise_districts_cumulative_statistics_response(self,
        day_wise_districts_cumulative_dtos:
            List[DistrictsDayWiseCumulativeStatisticsDto]):

        cumulative_day_wise_districts_dict_list = [
            self._convert_district_cumulative_statistics_dict_to_dto(
                district_wise_dto)
            for district_wise_dto in day_wise_districts_cumulative_dtos
        ]

        return cumulative_day_wise_districts_dict_list

    def raise_exception_for_invalid_mandal_id(self):
        raise BadRequest(*INVALID_MANDAL_ID)

    def raise_exception_for_invalid_positive_number(self):
        raise BadRequest(*INVALID_POSITIVE_NUMBER)

    def get_state_statistics_on_given_date_response(self,
        state_statistics_dto: List[StateStatisticsDto]):

        district_statistics_dicts_list = [
            self._convert_district_statistics_dtos_to_dict(
                district_dto=district_dto)
            for district_dto in state_statistics_dto.districts
        ]

        response = self._convert_state_statistics_dto_to_dict(
            state_statistics_dto=state_statistics_dto,
            district_statistics_dicts_list=district_statistics_dicts_list
        )

        return response

    def get_district_cumulative_statistics_response(self,
        district_cumulative_statistics_dto: DistrictCumulativeStatisticsDto):

        mandal_cumulative_dicts_list = [
            self._convert_mandal_cumulative_statistics_dtos_to_dict(
                mandal_dto=mandal_dto)
            for mandal_dto in district_cumulative_statistics_dto.mandals
        ]

        response = self._convert_district_cumulative_statistics_dto_to_dict(
            district_cumulative_statistics_dto=district_cumulative_statistics_dto,
            mandal_cumulative_dicts_list=mandal_cumulative_dicts_list
        )

        return response

    def raise_exception_for_invalid_district(self):
        raise BadRequest(*INVALID_DISTRICT_ID)

    def get_day_wise_state_statistics_response(self,
        day_wise_state_statistics_dtos: List[StateDayWiseStatisticsDto]):

        state_dto = day_wise_state_statistics_dtos[0]
        state_name = state_dto.name
        day_wise_statistics_dict_list = [
            self._convert_day_wise_statistics_dict_to_dto(day_wise_dto)
            for day_wise_dto in day_wise_state_statistics_dtos
        ]

        response = {
            "name": state_name,
            "day_wise_details": day_wise_statistics_dict_list
        }

        return response

    def get_daily_statistics_response(self,
        daily_statistics_dtos: List[DailyStatisticsDto]):

        response = [
            self._convert_daily_statistics_dto_to_dict(daily_statistics_dto)
            for daily_statistics_dto in daily_statistics_dtos
        ]

        return response

    def get_day_wise_district_cumulative_statistics_response(self,
        day_wise_district_cumulative_dto:
            DistrictDayWiseCumulativeStatisticsDto):

        name = day_wise_district_cumulative_dto.name
        day_wise_district_statistics = \
            day_wise_district_cumulative_dto.date_wise_details

        day_wise_statistics_dict_list = [
            self._convert_day_wise_cumulative_statistics_dict_to_dto(
                day_wise_dto)
            for day_wise_dto in day_wise_district_statistics
        ]

        response = {
            "name": name,
            "date_wise_details": day_wise_statistics_dict_list
        }

        return response

    def get_district_statistics_on_given_date_response(self,
        district_statistics_on_date_dto: DistrictOnDateStatisticsDto):

        mandal_statistics_dicts_list = [
            self._convert_mandal_statistics_dtos_to_dict(
                mandal_dto=mandal_dto)
            for mandal_dto in district_statistics_on_date_dto.mandals
        ]

        response = self._convert_district_statistics_dto_to_dict(
            district_statistics_dto=district_statistics_on_date_dto,
            mandal_statistics_dicts_list=mandal_statistics_dicts_list
        )

        return response

    def get_day_wise_mandals_cumulative_statistics_response(self, 
        day_wise_mandals_cumulative_dtos:
            List[MandalsDayWiseCumulativeStatisticsDto]):

        cumulative_day_wise_mandals_dict_list = [
            self._convert_mandal_cumulative_statistics_dict_to_dto(
                mandal_wise_dto)
            for mandal_wise_dto in day_wise_mandals_cumulative_dtos
        ]

        return cumulative_day_wise_mandals_dict_list

    def get_day_wise_district_statistics_response(self,
        day_wise_district_statistics_dtos: List[DistrictDailyStatisticsDto]):

        district_dto = day_wise_district_statistics_dtos[0]
        district_name = district_dto.name
        day_wise_statistics_dict_list = [
            self._convert_day_wise_statistics_dict_to_dto(day_wise_dto)
            for day_wise_dto in day_wise_district_statistics_dtos
        ]

        response = {
            "name": district_name,
            "day_wise_details": day_wise_statistics_dict_list
        }

        return response

    def get_district_wise_zone_details_response(self,
        green_zone_dtos_list: List[DistrictZonesDto],
        orange_zone_dtos_list: List[DistrictZonesDto],
        red_zone_dtos_list: List[DistrictZonesDto]):

        green_zone_dicts_list = [
            self._convert_green_zone_dto_green_zone_dict(district_dto)
            for district_dto in green_zone_dtos_list
        ]

        orange_zone_dicts_list = [
            self._convert_orange_zone_dto_orange_zone_dict(district_dto)
            for district_dto in orange_zone_dtos_list
        ]

        red_zone_dicts_list = [
            self._convert_red_zone_dto_red_zone_dict(district_dto)
            for district_dto in red_zone_dtos_list
        ]

        overall_zones_list = green_zone_dicts_list + orange_zone_dicts_list + \
            red_zone_dicts_list

        return overall_zones_list

    def _convert_district_cumulative_statistics_dict_to_dto(self,
        district_wise_dto):

        district_details_dict = {}
        district_details_dict['district_id'] = district_wise_dto.district_id
        district_details_dict['name'] = district_wise_dto.name

        date_wise_details_dicts_list = [
            self._convert_day_wise_cumulative_statistics_dict_to_dto(
                date_wise_dto)
            for date_wise_dto in district_wise_dto.date_wise_details
        ]

        district_details_dict['date_wise_details'] = \
            date_wise_details_dicts_list

        return district_details_dict

    def _convert_mandal_cumulative_statistics_dict_to_dto(self,
        mandal_wise_dto):

        mandal_details_dict = {}
        mandal_details_dict['mandal_id'] = mandal_wise_dto.mandal_id
        mandal_details_dict['name'] = mandal_wise_dto.name

        date_wise_details_dicts_list = [
            self._convert_day_wise_cumulative_statistics_dict_to_dto(
                date_wise_dto)
            for date_wise_dto in mandal_wise_dto.date_wise_details
        ]

        mandal_details_dict['date_wise_details'] = \
            date_wise_details_dicts_list

        return mandal_details_dict

    @staticmethod
    def _convert_district_statistics_dto_to_dict(
        district_statistics_dto, mandal_statistics_dicts_list):
        district_statistics_dict = {
            "name": district_statistics_dto.name,
            "total_confirmed": district_statistics_dto.total_confirmed,
            "total_deaths": district_statistics_dto.total_deaths,
            "total_recovered": district_statistics_dto.total_recovered,
            "mandals": mandal_statistics_dicts_list
        }
        return district_statistics_dict

    @staticmethod
    def _convert_district_statistics_dtos_to_dict(district_dto):
        district_dict = {
            "district_id": district_dto.district_id,
            "name": district_dto.name,
            "total_confirmed": district_dto.total_confirmed,
            "total_deaths": district_dto.total_deaths,
            "total_recovered": district_dto.total_recovered
        }
        return district_dict

    @staticmethod
    def _convert_mandal_statistics_dtos_to_dict(mandal_dto):
        mandal_dict = {
            "mandal_id": mandal_dto.mandal_id,
            "name": mandal_dto.name,
            "total_confirmed": mandal_dto.total_confirmed,
            "total_deaths": mandal_dto.total_deaths,
            "total_recovered": mandal_dto.total_recovered
        }
        return mandal_dict

    @staticmethod
    def _convert_district_cumulative_statistics_dtos_to_dict(district_dto):
        district_dict = {
            "district_id": district_dto.district_id,
            "name": district_dto.name,
            "total_confirmed": district_dto.total_confirmed,
            "total_deaths": district_dto.total_deaths,
            "total_recovered": district_dto.total_recovered,
            "total_active": district_dto.total_active
        }
        return district_dict

    @staticmethod
    def _convert_mandal_cumulative_statistics_dtos_to_dict(mandal_dto):
        mandal_dict = {
            "mandal_id": mandal_dto.mandal_id,
            "name": mandal_dto.name,
            "total_confirmed": mandal_dto.total_confirmed,
            "total_deaths": mandal_dto.total_deaths,
            "total_recovered": mandal_dto.total_recovered,
            "total_active": mandal_dto.total_active
        }
        return mandal_dict

    @staticmethod
    def _convert_state_cumulative_statistics_dto_to_dict(
        state_cumulative_statistics_dto, district_cumulative_dicts_list):

        state_cumulative_statistics_dict = {
            'name': state_cumulative_statistics_dto.name,
            'total_confirmed':
                state_cumulative_statistics_dto.total_confirmed,
            'total_deaths':
                state_cumulative_statistics_dto.total_deaths,
            'total_recovered':
                state_cumulative_statistics_dto.total_recovered,
            'total_active':
                state_cumulative_statistics_dto.total_active,
            'districts': district_cumulative_dicts_list
        }
        return state_cumulative_statistics_dict

    @staticmethod
    def _convert_district_cumulative_statistics_dto_to_dict(
        district_cumulative_statistics_dto, mandal_cumulative_dicts_list):

        district_cumulative_statistics_dict = {
            'name': district_cumulative_statistics_dto.name,
            'total_confirmed':
                district_cumulative_statistics_dto.total_confirmed,
            'total_deaths':
                district_cumulative_statistics_dto.total_deaths,
            'total_recovered':
                district_cumulative_statistics_dto.total_recovered,
            'total_active':
                district_cumulative_statistics_dto.total_active,
            'mandals': mandal_cumulative_dicts_list
        }
        return district_cumulative_statistics_dict

    @staticmethod
    def _convert_state_statistics_dto_to_dict(
        state_statistics_dto, district_statistics_dicts_list):

        state_statistics_dict = {
            'name': state_statistics_dto.name,
            'total_confirmed':
                state_statistics_dto.total_confirmed,
            'total_deaths':
                state_statistics_dto.total_deaths,
            'total_recovered':
                state_statistics_dto.total_recovered,
            'districts': district_statistics_dicts_list
        }
        return state_statistics_dict

    @staticmethod
    def _convert_day_wise_statistics_dict_to_dto(
        day_wise_statistics_dto):

        till_date = day_wise_statistics_dto.till_date

        day_wise_statistics_dict = {
            "for_date": till_date.strftime(DateFormat.DATEFORMAT.value),
            "total_confirmed": day_wise_statistics_dto.total_confirmed,
            "total_deaths": day_wise_statistics_dto.total_deaths,
            "total_recovered": day_wise_statistics_dto.total_recovered,
        }
        return day_wise_statistics_dict

    @staticmethod
    def _convert_day_wise_cumulative_statistics_dict_to_dto(
        day_wise_statistics_dto):

        till_date = day_wise_statistics_dto.till_date

        day_wise_statistics_dict = {
            "till_date": till_date.strftime(DateFormat.DATEFORMAT.value),
            "total_confirmed": day_wise_statistics_dto.total_confirmed,
            "total_deaths": day_wise_statistics_dto.total_deaths,
            "total_recovered": day_wise_statistics_dto.total_recovered,
            "total_active": day_wise_statistics_dto.total_active
        }
        return day_wise_statistics_dict

    @staticmethod
    def _convert_daily_statistics_dto_to_dict(daily_statistics_dto):

        for_date = daily_statistics_dto.for_date

        daily_statistics_dto = {
            "for_date": for_date.strftime(DateFormat.DATEFORMAT.value),
            "district_id": daily_statistics_dto.district_id,
            "district_name": daily_statistics_dto.district_name,
            "mandal_id": daily_statistics_dto.mandal_id,
            "mandal_name": daily_statistics_dto.mandal_name,
            "total_confirmed": daily_statistics_dto.total_confirmed,
            "total_deaths": daily_statistics_dto.total_deaths,
            "total_recovered": daily_statistics_dto.total_recovered
        }

        return daily_statistics_dto

    @staticmethod
    def _convert_green_zone_dto_green_zone_dict(district_dto):
        green_zone_dict = {
            "district_id": district_dto.district_id,
            "name": district_dto.name,
            "zone": DistrictZones.GREEN.value
        }
        return green_zone_dict

    @staticmethod
    def _convert_orange_zone_dto_orange_zone_dict(district_dto):
        orange_zone_dict = {
            "district_id": district_dto.district_id,
            "name": district_dto.name,
            "zone": DistrictZones.ORANGE.value
        }
        return orange_zone_dict

    @staticmethod
    def _convert_red_zone_dto_red_zone_dict(district_dto):
        red_zone_dict = {
            "district_id": district_dto.district_id,
            "name": district_dto.name,
            "zone": DistrictZones.RED.value
        }
        return red_zone_dict
