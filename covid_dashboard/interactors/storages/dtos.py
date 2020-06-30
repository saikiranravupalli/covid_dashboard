from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass()
class UserDetailsDTO:
    user_id: int
    is_admin: bool

@dataclass()
class MandalStatisticsDto:
    mandal_id: int
    name: str
    total_confirmed: int
    total_deaths: int
    total_recovered: int

@dataclass()
class DailyStatisticsDto:
    for_date: date
    district_id: int
    district_name: str
    mandal_id: str
    mandal_name: str
    total_confirmed: int
    total_deaths: int
    total_recovered: int

@dataclass()
class MandalActiveCasesDto(MandalStatisticsDto):
    total_active: int

@dataclass()
class DistrictStatisticsDto:
    district_id: int
    name: str
    total_confirmed: int
    total_deaths: int
    total_recovered: int

@dataclass()
class DistrictActiveCasesDto(DistrictStatisticsDto):
    total_active: int

@dataclass()
class StateCumulativeStatisticsDto:
    name: str
    total_confirmed: int
    total_deaths: int
    total_recovered: int
    total_active: int
    districts: List[DistrictActiveCasesDto]

@dataclass()
class CommonStatisticsDto:
    name: str
    till_date: date
    total_confirmed: int
    total_deaths: int
    total_recovered: int

@dataclass()
class StateDayWiseStatisticsDto(CommonStatisticsDto):
    pass

@dataclass()
class DistrictDailyStatisticsDto(CommonStatisticsDto):
    pass

@dataclass()
class StateDayWiseCumulativeStatisticsDto(StateDayWiseStatisticsDto):
    total_active: int

@dataclass()
class DistrictDayWiseStatisticsDto:
    till_date: date
    total_confirmed: int
    total_deaths: int
    total_recovered: int
    total_active: int

@dataclass()
class MandalDayWiseStatisticsDto:
    till_date: date
    total_confirmed: int
    total_deaths: int
    total_recovered: int
    total_active: int

@dataclass()
class MandalsDayWiseCumulativeStatisticsDto:
    mandal_id: int
    name: str
    date_wise_details: List[MandalDayWiseStatisticsDto]

@dataclass()
class DistrictDayWiseCumulativeStatisticsDto:
    name: str
    date_wise_details: List[DistrictDayWiseStatisticsDto]

@dataclass()
class DistrictsDayWiseCumulativeStatisticsDto(
    DistrictDayWiseCumulativeStatisticsDto):
    district_id: int

@dataclass()
class StateStatisticsDto:
    name: str
    total_confirmed: int
    total_deaths: int
    total_recovered: int
    districts: List[DistrictStatisticsDto]

@dataclass()
class DistrictCumulativeStatisticsDto():
    name: str
    total_confirmed: int
    total_deaths: int
    total_recovered: int
    total_active: int
    mandals: List[MandalActiveCasesDto]

@dataclass()
class DistrictOnDateStatisticsDto:
    name: str
    total_confirmed: int
    total_deaths: int
    total_recovered: int
    mandals: List[MandalStatisticsDto]

@dataclass()
class DistrictZonesDto:
    district_id: int
    name: str
    active_cases: int
