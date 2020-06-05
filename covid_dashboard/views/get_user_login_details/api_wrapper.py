import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from common.oauth2_storage import OAuth2SQLStorage
from covid_dashboard.interactors.login_interactor import \
    LoginInteractor
from covid_dashboard.storages.user_storage_implementation import \
    UserStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    storage = UserStorageImplementation()
    oauth2_storage = OAuth2SQLStorage()
    presenter = PresenterImplementation()

    interactor = LoginInteractor(
        storage=storage,
        oauth2storage=oauth2_storage,
        presenter=presenter
    )

    response = interactor.login(
        username=request_data['username'],
        password=request_data['password']
    )

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
