from covid_dashboard.exceptions.exceptions import InvalidAccess
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.adapters.service_adapter import get_service_adapter

class DailyStatisticsInteractor:

    def __init__(self, storage: MandalStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_daily_statistics(self, user_id: int):

        service_adapter = get_service_adapter()

        user_details_dto = \
            service_adapter.auth_service.get_user_dto(user_id=user_id)

        is_user_admin = user_details_dto.is_admin
        is_invalid_user_admin = not is_user_admin

        if is_invalid_user_admin:
            self.presenter.raise_exception_for_invalid_user_admin()

        daily_statistics_dtos = \
            self.storage.get_daily_statistics()

        response = self.presenter.get_daily_statistics_response(
            daily_statistics_dtos=daily_statistics_dtos
        )

        return response
