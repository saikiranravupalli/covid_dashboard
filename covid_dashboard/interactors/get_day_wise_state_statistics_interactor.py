from datetime import date, timedelta
from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.storages.dtos import \
    StateDayWiseStatisticsDto

class StateDayWiseStatisticsInteractor:

    def __init__(self, storage: StateStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_state_statistics(self):

        day_wise_state_statistics_dtos = \
            self.storage.get_day_wise_state_statistics()

        response = \
            self.presenter.get_day_wise_state_statistics_response(
                day_wise_state_statistics_dtos=day_wise_state_statistics_dtos
            )

        return response
