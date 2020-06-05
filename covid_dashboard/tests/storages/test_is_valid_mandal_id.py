import pytest

from covid_dashboard.models import Mandal
from covid_dashboard.exceptions.exceptions import InvalidMandal
from covid_dashboard.storages.mandal_storage_implementation import \
    MandalStorageImplementation

@pytest.mark.django_db
def test_is_valid_mandal_id_given_invalid_mandal_id_raises_invalid_mandal_exception():

    # Arrange
    mandal_id = -2
    storage = MandalStorageImplementation()

    # Act
    with pytest.raises(InvalidMandal):
        storage.is_valid_mandal_id(
            mandal_id=mandal_id
        )
