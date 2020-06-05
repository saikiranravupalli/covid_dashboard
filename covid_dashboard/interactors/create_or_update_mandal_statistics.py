from covid_dashboard.exceptions.exceptions import InvalidMandal, \
    InvalidMandalStatistics
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.storages.user_storage_interface import \
    UserStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface

class CreateOrUpdateMandalStatisticsInteractor:
    def __init__(self, mandal_storage: MandalStorageInterface,
                 user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.mandal_storage = mandal_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def create_or_update_mandal_statistics(self,
                                           user_id: int,
                                           for_date: str,
                                           total_confirmed: int,
                                           total_recovered: int,
                                           total_deaths: int,
                                           mandal_id: int):

        self._check_is_valid_input(total_confirmed)
        self._check_is_valid_input(total_recovered)
        self._check_is_valid_input(total_deaths)
        self._check_is_valid_user_admin(user_id)
        self._check_is_valid_mandal_id(mandal_id)

        try:
            self.mandal_storage.is_mandal_stats_exists(for_date=for_date,
                                                         mandal_id=mandal_id)
        except InvalidMandalStatistics:
            self.mandal_storage.create_mandal_statistics(
                for_date=for_date, total_confirmed=total_confirmed,
                total_recovered=total_recovered, total_deaths=total_deaths,
                mandal_id=mandal_id)
        else:
            self.mandal_storage.update_mandal_statistics(
                for_date=for_date, total_confirmed=total_confirmed,
                total_recovered=total_recovered, total_deaths=total_deaths,
                mandal_id=mandal_id)

    def _check_is_valid_input(self, value):
        if value < 0:
            self.presenter.raise_exception_for_invalid_positive_number()

    def _check_is_valid_user_admin(self, user_id):
        is_user_admin = self.user_storage.is_user_admin(user_id)
        is_invalid_user_admin = not is_user_admin

        if is_invalid_user_admin:
            self.presenter.raise_exception_for_invalid_user_admin()

    def _check_is_valid_mandal_id(self, mandal_id):
        try:
            self.mandal_storage.is_valid_mandal_id(mandal_id)
        except InvalidMandal:
            self.presenter.raise_exception_for_invalid_mandal_id()
