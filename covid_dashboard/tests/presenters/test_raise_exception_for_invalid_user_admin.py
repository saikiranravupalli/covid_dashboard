import pytest
from django_swagger_utils.drf_server.exceptions import Forbidden

from covid_dashboard.exceptions.exception_messages import INVALID_ACCESS
from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_raise_exception_for_invalid_admin_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_ACCESS[0]
    exception_res_status = INVALID_ACCESS[1]

    # Act
    with pytest.raises(Forbidden) as exception:
        presenter.raise_exception_for_invalid_user_admin()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
