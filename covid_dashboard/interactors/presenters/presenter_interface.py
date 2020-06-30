from abc import ABC, abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import \
    StateCumulativeStatisticsDto, StateDayWiseCumulativeStatisticsDto, \
    DistrictsDayWiseCumulativeStatisticsDto, DistrictActiveCasesDto, \
    StateStatisticsDto, DistrictCumulativeStatisticsDto, \
    StateDayWiseStatisticsDto, DailyStatisticsDto, \
    DistrictDayWiseCumulativeStatisticsDto, DistrictOnDateStatisticsDto, \
    MandalsDayWiseCumulativeStatisticsDto, DistrictDailyStatisticsDto, \
    DistrictZonesDto
class PresenterInterface(ABC):

    @abstractmethod
    def get_state_cumulative_statistics_response(self, 
        state_cumulative_statistics_dto: StateCumulativeStatisticsDto):
        pass

    @abstractmethod
    def get_day_wise_state_cumulative_statistics_response(self,
        day_wise_state_cumulative_dtos=
            List[StateDayWiseCumulativeStatisticsDto]):
        pass

    @abstractmethod
    def get_day_wise_districts_cumulative_statistics_response(self,
        day_wise_districts_cumulative_dtos=
            List[DistrictsDayWiseCumulativeStatisticsDto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_admin(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_mandal_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_positive_number(self):
        pass

    @abstractmethod
    def get_state_statistics_on_given_date_response(self,
        state_statistics_dto: StateStatisticsDto):
        pass

    @abstractmethod
    def get_district_cumulative_statistics_response(self,
        district_cumulative_statistics_dto: DistrictCumulativeStatisticsDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_district(self):
        pass

    @abstractmethod
    def get_day_wise_state_statistics_response(self,
        day_wise_state_statistics_dtos: List[StateDayWiseStatisticsDto]):
        pass

    @abstractmethod
    def get_daily_statistics_response(self,
        daily_statistics_dtos: List[DailyStatisticsDto]):
        pass

    @abstractmethod
    def get_day_wise_district_cumulative_statistics_response(self,
        day_wise_district_cumulative_dto:
            DistrictDayWiseCumulativeStatisticsDto):
        pass

    @abstractmethod
    def get_district_statistics_on_given_date_response(self,
        district_statistics_on_date_dto: DistrictOnDateStatisticsDto):
        pass

    @abstractmethod
    def get_day_wise_mandals_cumulative_statistics_response(self, 
        day_wise_mandals_cumulative_dtos:
            List[MandalsDayWiseCumulativeStatisticsDto]):
        pass

    @abstractmethod
    def get_day_wise_district_statistics_response(self,
        day_wise_district_statistics_dtos: List[DistrictDailyStatisticsDto]):
        pass

    @abstractmethod
    def get_district_wise_zone_details_response(self,
        green_zone_dtos_list=List[DistrictZonesDto],
        orange_zone_dtos_list=List[DistrictZonesDto],
        red_zone_dtos_list=List[DistrictZonesDto]):
        pass