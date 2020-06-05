from datetime import date, timedelta
from covid_dashboard.interactors.storages.dtos import \
    StateDayWiseCumulativeStatisticsDto
from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class StateDayWiseCumulativeStatisticsInteractor:
    total_confirmed = 0
    total_deaths = 0
    total_recovered = 0
    total_active = 0

    def __init__(self, storage: StateStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_state_cumulative_statistics(self):

        day_wise_state_statistics_dtos = \
            self.storage.get_day_wise_state_cumulative_statistics()

        updated_cumulative_statistics_dtos = \
            self._add_day_wise_cumulative_statics(
                day_wise_state_statistics_dtos
            )

        response = \
            self.presenter.get_day_wise_state_cumulative_statistics_response(
                day_wise_state_cumulative_dtos=
                    updated_cumulative_statistics_dtos
            )

        return response

    def _add_day_wise_cumulative_statics(self, day_wise_state_statistics_dtos):

        updated_cumulative_statistics = [
            self._add_cumulative_data(state)
            for state in day_wise_state_statistics_dtos
        ]

        return updated_cumulative_statistics

    def _add_cumulative_data(self, state_dto):
        state_dto.total_confirmed += self.total_confirmed
        state_dto.total_deaths += self.total_deaths
        state_dto.total_recovered += self.total_recovered
        state_dto.total_active += self.total_active

        self.total_confirmed = state_dto.total_confirmed
        self.total_deaths = state_dto.total_deaths
        self.total_recovered = state_dto.total_recovered
        self.total_active = state_dto.total_active

        return state_dto
