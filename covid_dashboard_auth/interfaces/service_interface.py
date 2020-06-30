from typing import List

from covid_dashboard_auth.interactors.get_user_details_interactor import \
    GetUserDetailsInteractor
from covid_dashboard_auth.storages.user_storage_implementation import \
    UserStorageImplementation


class ServiceInterface:

    @staticmethod
    def get_user_dto(user_id: int):
        storage = UserStorageImplementation()
        interactor = GetUserDetailsInteractor(storage=storage)
        user_dto = interactor.get_user_details_dto(user_id=user_id)
        return user_dto
