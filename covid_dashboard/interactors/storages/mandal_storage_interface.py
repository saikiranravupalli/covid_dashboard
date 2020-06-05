from abc import ABC, abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import \
    DailyStatisticsDto, DistrictOnDateStatisticsDto, \
    MandalsDayWiseCumulativeStatisticsDto

class MandalStorageInterface(ABC):

    @abstractmethod
    def is_valid_mandal_id(self, mandal_id: int):
        pass

    @abstractmethod
    def is_mandal_stats_exists(self, for_date: str, mandal_id: int):
        pass

    @abstractmethod
    def update_mandal_statistics(
        self,
        for_date: int,
        total_confirmed: int,
        total_recovered: int,
        total_deaths: int,
        mandal_id: int
    ):
        pass

    @abstractmethod
    def create_mandal_statistics(
        self,
        for_date: int,
        total_confirmed: int,
        total_recovered: int,
        total_deaths: int,
        mandal_id: int
    ):
        pass

    @abstractmethod
    def get_daily_statistics(self) -> List[DailyStatisticsDto]:
        pass

    @abstractmethod
    def get_district_statistics_on_given_date(self,
                                              for_date: str,
                                              district_id: int) -> \
        DistrictOnDateStatisticsDto:
        pass

    @abstractmethod
    def get_day_wise_mandals_cumulative_statistics(self, district_id: int) \
        -> List[MandalsDayWiseCumulativeStatisticsDto]:
        pass
