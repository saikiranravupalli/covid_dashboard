from covid_dashboard.exceptions.exceptions import InvalidAccess
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.storages.user_storage_interface import \
    UserStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class DailyStatisticsInteractor:

    def __init__(self, storage: MandalStorageInterface,
                 user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.user_storage = user_storage
        self.presenter = presenter

    def get_daily_statistics(self, user_id: int):

        is_user_admin = self.user_storage.is_user_admin(user_id)
        is_user_not_admin = not is_user_admin

        if is_user_not_admin:
            self.presenter.raise_exception_for_invalid_user_admin()

        daily_statistics_dtos = \
            self.storage.get_daily_statistics()

        response = self.presenter.get_daily_statistics_response(
            daily_statistics_dtos=daily_statistics_dtos
        )

        return response
