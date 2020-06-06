import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_district_wise_zone_details_interactor import \
    GetDistrictWiseZoneDetailsInteractor
from covid_dashboard.storages.state_storage_implementation import \
    StateStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = StateStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetDistrictWiseZoneDetailsInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.get_district_wise_zone_details()

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
