import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.create_or_update_mandal_statistics import \
    CreateOrUpdateMandalStatisticsInteractor
from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs['request_data']

    mandal_storage = MandalStorageImplementation()
    presenter = PresenterImplementation()

    user_id = user.id
    for_date = request_data['for_date']
    total_confirmed = request_data['total_confirmed']
    total_recovered = request_data['total_recovered']
    total_deaths = request_data['total_deaths']
    mandal_id = kwargs['mandal_id']

    interactor = CreateOrUpdateMandalStatisticsInteractor(
        mandal_storage=mandal_storage,
        presenter=presenter
    )

    interactor.create_or_update_mandal_statistics(
        user_id=user_id,
        for_date=for_date,
        total_confirmed=total_confirmed,
        total_recovered=total_recovered,
        total_deaths=total_deaths,
        mandal_id=mandal_id
    )

    return HttpResponse(status=201)
