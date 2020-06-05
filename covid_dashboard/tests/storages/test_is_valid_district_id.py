import pytest

from covid_dashboard.models import Mandal
from covid_dashboard.exceptions.exceptions import InvalidDistrict
from covid_dashboard.storages.district_storage_implementation import \
    DistrictStorageImplementation

@pytest.mark.django_db
def test_is_valid_district_id_given_invalid_district_id_raises_exception():

    # Arrange
    district_id = -2
    storage = DistrictStorageImplementation()

    # Act
    with pytest.raises(InvalidDistrict):
        storage.is_valid_district_id(
            district_id=district_id
        )
