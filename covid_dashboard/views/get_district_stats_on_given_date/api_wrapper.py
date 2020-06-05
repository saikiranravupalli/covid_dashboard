import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors\
    .get_day_wise_district_details_on_given_date_interactor import \
        DistrictStatisticsInteractor
from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation
from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    district_id = kwargs['district_id']
    request_data = kwargs['request_data']
    for_date = request_data['for_date']
    district_storage = DistrictStorageImplementation()
    mandal_storage = MandalStorageImplementation()
    presenter = PresenterImplementation()

    interactor = DistrictStatisticsInteractor(
        district_storage=district_storage,
        mandal_storage=mandal_storage,
        presenter=presenter
    )

    response = \
        interactor.get_district_statistics_on_given_date(
            district_id=district_id,
            for_date=for_date
        )

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=200)
