from abc import ABC, abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import \
    StateCumulativeStatisticsDto, StateDayWiseCumulativeStatisticsDto, \
    StateStatisticsDto, StateDayWiseStatisticsDto

class StateStorageInterface(ABC):

    @abstractmethod
    def get_state_cumulative_statistics(self, till_date: str)\
        -> StateCumulativeStatisticsDto:
        pass

    @abstractmethod
    def get_day_wise_state_cumulative_statistics(self) \
        -> List[StateDayWiseCumulativeStatisticsDto]:
        pass

    @abstractmethod
    def get_state_statistics_on_given_date(self, for_date: str) -> \
        StateStatisticsDto:
        pass

    @abstractmethod
    def get_day_wise_state_statistics(self) -> \
        List[StateDayWiseStatisticsDto]:
        pass
