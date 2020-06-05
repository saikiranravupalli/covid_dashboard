import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest

from covid_dashboard.exceptions.exception_messages import INVALID_DISTRICT_ID
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_raise_exception_for_invalid_district_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_DISTRICT_ID[0]
    exception_res_status = INVALID_DISTRICT_ID[1]

    # Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_district()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
