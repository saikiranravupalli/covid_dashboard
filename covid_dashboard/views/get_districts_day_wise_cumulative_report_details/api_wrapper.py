import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.districts_day_wise_cumulative_statistics_interactor import \
    DistrictsDayWiseCumulativeStatisticsInteractor
from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = DistrictStorageImplementation()
    presenter = PresenterImplementation()

    interactor = DistrictsDayWiseCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.get_day_wise_districts_cumulative_statistics()

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
