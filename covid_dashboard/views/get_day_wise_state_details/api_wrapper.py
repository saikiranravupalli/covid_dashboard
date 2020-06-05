import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_day_wise_state_statistics_interactor import \
    StateDayWiseStatisticsInteractor
from covid_dashboard.storages.state_storage_implementation import \
    StateStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = StateStorageImplementation()
    presenter = PresenterImplementation()

    interactor = StateDayWiseStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )
    response = interactor.get_day_wise_state_statistics()

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
