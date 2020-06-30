import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest, Forbidden
from covid_dashboard.exceptions.exception_messages import INVALID_USERNAME, \
    INVALID_PASSWORD
from covid_dashboard_auth.interactors.presenters.presenter_interface import \
    PresenterInterface

class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self):
        raise BadRequest(*INVALID_USERNAME)

    def raise_exception_for_invalid_password(self):
        raise BadRequest(*INVALID_PASSWORD)

    def get_response_for_login(self, tokens_dto, is_admin: bool):
        response = {
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "is_admin": is_admin
        }
        return response
