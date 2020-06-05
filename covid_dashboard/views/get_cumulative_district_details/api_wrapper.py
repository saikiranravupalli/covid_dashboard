import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors\
    .get_cumulative_district_details_with_mandals_interactor import \
        DistrictCumulativeStatisticsInteractor
from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    till_date = request_data['till_date']
    district_id = kwargs['district_id']
    storage = DistrictStorageImplementation()
    presenter = PresenterImplementation()

    interactor = DistrictCumulativeStatisticsInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.get_district_cumulative_statistics(
        till_date=till_date,
        district_id=district_id
    )

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
