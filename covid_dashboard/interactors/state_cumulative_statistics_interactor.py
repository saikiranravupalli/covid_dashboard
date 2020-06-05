from datetime import date
from covid_dashboard.interactors.storages.state_storage_interface import \
    StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class StateCumulativeStatisticsInteractor:

    def __init__(self, storage: StateStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_state_cumulative_statistics(self, till_date: str):

        state_cumulative_statistics_dto = \
            self.storage.get_state_cumulative_statistics(
                till_date=till_date
            )

        if state_cumulative_statistics_dto is None:
            response = self._make_alternate_response()
        else:
            response = \
                self.presenter.get_state_cumulative_statistics_response(
                    state_cumulative_statistics_dto=
                    state_cumulative_statistics_dto
                )

        return response

    def _make_alternate_response(self):
        response = {
            "name": "AndhraPradesh",
            "total_confirmed": 0,
            "total_active": 0,
            "total_deaths": 0,
            "total_recovered": 0,
            "districts": []
        }
        return response
