import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_state_stats_on_given_date_interactor \
    import StateStatisticsInteractor
from covid_dashboard.storages.state_storage_implementation import \
    StateStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    storage = StateStorageImplementation()
    presenter = PresenterImplementation()

    interactor = StateStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.get_state_statistics_on_given_date(
        for_date=request_data['for_date']
    )

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
