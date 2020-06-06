import math

from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class GetDistrictWiseZoneDetailsInteractor:

    def __init__(self, storage: StateStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_district_wise_zone_details(self):
        total_active_cases = 0
        districts_cumulative_dtos = \
            self.storage.get_district_wise_active_cases_details()

        for district_cumulative_dto in districts_cumulative_dtos:
            total_active_cases += district_cumulative_dto.active_cases

        one_third_active_cases = math.ceil(0.3*total_active_cases)
        green_zone_dtos_list, orange_zone_dtos_list, red_zone_dtos_list = \
            [], [], []

        for district_cumulative_dto in districts_cumulative_dtos:
            self._add_district_dto_to_its_corresponding_zone_list(
                green_zone_dtos_list, orange_zone_dtos_list,
                red_zone_dtos_list, district_cumulative_dto,
                one_third_active_cases)

        response = self.presenter.get_district_wise_zone_details_response(
            green_zone_dtos_list=green_zone_dtos_list,
            orange_zone_dtos_list=orange_zone_dtos_list,
            red_zone_dtos_list=red_zone_dtos_list)

        return response

    def _add_district_dto_to_its_corresponding_zone_list(self, 
        green_zone_dtos_list, orange_zone_dtos_list, red_zone_dtos_list,
        district_cumulative_dto, one_third_active_cases):

        active_cases = district_cumulative_dto.active_cases
        two_third_active_cases = 2 * one_third_active_cases

        if active_cases <=  one_third_active_cases:
            green_zone_dtos_list.append(district_cumulative_dto)
        elif (active_cases > one_third_active_cases and  
              active_cases <= two_third_active_cases):
            orange_zone_dtos_list.append(district_cumulative_dto)
        else:
            red_zone_dtos_list.append(district_cumulative_dto)
