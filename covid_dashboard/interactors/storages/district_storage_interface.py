from abc import ABC, abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import \
    DistrictsDayWiseCumulativeStatisticsDto, DistrictActiveCasesDto, \
    DistrictCumulativeStatisticsDto, DistrictDayWiseCumulativeStatisticsDto, \
    DistrictDailyStatisticsDto

class DistrictStorageInterface(ABC):

    @abstractmethod
    def get_day_wise_districts_cumulative_statistics(self) \
        -> List[DistrictsDayWiseCumulativeStatisticsDto]:
        pass

    @abstractmethod
    def is_valid_district_id(self, district_id: int):
        pass

    @abstractmethod
    def get_district_cumulative_statistics(self,
                                           till_date: str,
                                           district_id: int) -> \
        DistrictCumulativeStatisticsDto:
        pass

    @abstractmethod
    def get_day_wise_district_cumulative_statistics(self,
                                                    district_id: int) -> \
        DistrictDayWiseCumulativeStatisticsDto:
        pass

    @abstractmethod
    def get_day_wise_district_statistics(self, district_id: int) -> \
        List[DistrictDailyStatisticsDto]:
        pass
