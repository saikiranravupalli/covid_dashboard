import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_daily_statistics_interactor import \
        DailyStatisticsInteractor
from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id
    mandal_storage = MandalStorageImplementation()
    presenter = PresenterImplementation()

    interactor = DailyStatisticsInteractor(
        storage=mandal_storage,
        presenter=presenter
    )

    response = interactor.get_daily_statistics(user_id=user_id)

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
