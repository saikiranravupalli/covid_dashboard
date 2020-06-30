import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest, Forbidden
from unittest.mock import create_autospec, patch

from covid_dashboard.exceptions.exceptions import InvalidMandal, \
    InvalidMandalStatistics
from covid_dashboard.interactors.storages.mandal_storage_interface import \
    MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from covid_dashboard.interactors.create_or_update_mandal_statistics import \
    CreateOrUpdateMandalStatisticsInteractor
from covid_dashboard_auth.interactors.storages.dtos import UserDetailsDTO

class TestCreateOrUpdateMandalStatisticsInteractor:

    @patch('covid_dashboard_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
    def test_given_invalid_admin_raises_exception(self, get_user_dto):

        # Arrange
        invalid_user_admin = 1
        mandal_id = 1
        for_date="2020/05/27"
        total_confirmed=10
        total_recovered=2
        total_deaths=3
        mandal_storage = create_autospec(MandalStorageInterface)
        presenter = create_autospec(PresenterInterface)
        get_user_dto.return_value = UserDetailsDTO(
            user_id=1,
            is_admin=False
        )
        presenter.raise_exception_for_invalid_user_admin.side_effect = \
            Forbidden

        interactor = CreateOrUpdateMandalStatisticsInteractor(
            mandal_storage=mandal_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(Forbidden):
            interactor.create_or_update_mandal_statistics(
                user_id=invalid_user_admin,
                for_date=for_date,
                total_confirmed=total_confirmed,
                total_recovered=total_recovered,
                total_deaths=total_deaths,
                mandal_id=mandal_id
            )

        # Assert
        presenter.raise_exception_for_invalid_user_admin.assert_called_once()

    @patch('covid_dashboard_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
    def test_given_invalid_mandal_id_raises_exception(self, get_user_dto):

        # Arrange
        invalid_mandal_id = -1
        user_id = 1
        for_date="2020/05/27"
        total_confirmed=10
        total_recovered=2
        total_deaths=3
        mandal_storage = create_autospec(MandalStorageInterface)
        presenter = create_autospec(PresenterInterface)
        get_user_dto.return_value = UserDetailsDTO(
            user_id=1,
            is_admin=True
        )
        mandal_storage.is_valid_mandal_id.side_effect = InvalidMandal
        presenter.raise_exception_for_invalid_mandal_id.side_effect = \
            BadRequest

        interactor = CreateOrUpdateMandalStatisticsInteractor(
            mandal_storage=mandal_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(BadRequest):
            interactor.create_or_update_mandal_statistics(
                user_id=user_id,
                for_date=for_date,
                total_confirmed=total_confirmed,
                total_recovered=total_recovered,
                total_deaths=total_deaths,
                mandal_id=invalid_mandal_id
            )

        # Assert
        mandal_storage.is_valid_mandal_id.assert_called_once_with(
            mandal_id=invalid_mandal_id
        )
        presenter.raise_exception_for_invalid_mandal_id.assert_called_once()

    @pytest.mark.parametrize(
        "user_id, mandal_id, total_confirmed, total_recovered, total_deaths, for_date", 
        [
            (1, 1, -1, 10, 3, "2020/05/27"), (1, 1, 1, -2, 3, "2020/05/27"), 
            (1, 1, 1, 2, -3, "2020/05/27")
        ]
    )
    def test_given_negative_input_values_raises_exception(self,
                                                          user_id,
                                                          mandal_id,
                                                          total_confirmed,
                                                          total_recovered,
                                                          total_deaths,
                                                          for_date):
        # Arrange
        mandal_id = mandal_id
        for_date=for_date
        invalid_total_confirmed=total_confirmed
        total_recovered=total_recovered
        total_deaths=total_deaths
        mandal_storage = create_autospec(MandalStorageInterface)
        presenter = create_autospec(PresenterInterface)
        presenter.raise_exception_for_invalid_positive_number.side_effect = \
            BadRequest

        interactor = CreateOrUpdateMandalStatisticsInteractor(
            mandal_storage=mandal_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(BadRequest):
            interactor.create_or_update_mandal_statistics(
                user_id=user_id,
                for_date=for_date,
                total_confirmed=invalid_total_confirmed,
                total_recovered=total_recovered,
                total_deaths=total_deaths,
                mandal_id=mandal_id
            )

        # Assert
        presenter.raise_exception_for_invalid_positive_number\
                 .assert_called_once()

    @patch('covid_dashboard_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
    @pytest.mark.parametrize(
        "user_id, mandal_id, total_confirmed, total_recovered, total_deaths, for_date",
        [
            (1, 1, 100, 10, 3, "2020/05/27"), (1, 1, 1, 2, 0, "2020/05/27")
        ]
    )
    def test_given_positive_number_or_zero_as_input_creates_mandal_statistics(self,
        get_user_dto, user_id, mandal_id, total_confirmed, total_recovered,
        total_deaths, for_date):

        # Arrange
        mandal_id = mandal_id
        for_date=for_date
        total_confirmed=total_confirmed
        total_recovered=total_recovered
        total_deaths=total_deaths
        user_details_dto = UserDetailsDTO(
            user_id=1,
            is_admin=True
        )
        mandal_storage = create_autospec(MandalStorageInterface)
        presenter = create_autospec(PresenterInterface)
        mandal_storage.is_mandal_stats_exists.side_effect = \
            InvalidMandalStatistics

        get_user_dto.return_value = user_details_dto
        interactor = CreateOrUpdateMandalStatisticsInteractor(
            mandal_storage=mandal_storage,
            presenter=presenter
        )

        # Act
        interactor.create_or_update_mandal_statistics(
            user_id=user_id,
            for_date=for_date,
            total_confirmed=total_confirmed,
            total_recovered=total_recovered,
            total_deaths=total_deaths,
            mandal_id=mandal_id
        )

        # Assert
        mandal_storage.is_valid_mandal_id.assert_called_once_with(
            mandal_id=mandal_id
        )
        mandal_storage.is_mandal_stats_exists.assert_called_once_with(
            mandal_id=mandal_id, for_date=for_date
        )
        mandal_storage.create_mandal_statistics.assert_called_once_with(
            for_date=for_date,
            total_confirmed=total_confirmed,
            total_recovered=total_recovered,
            total_deaths=total_deaths,
            mandal_id=mandal_id
        )

    @patch('covid_dashboard_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
    def test_given_update_mandal_stats_if_already_exists_results_update_reaction(self, get_user_dto):

        # Arrange
        mandal_id = 1
        user_id=1
        for_date="2020/05/27"
        total_confirmed=10
        total_recovered=2
        total_deaths=3
        get_user_dto.return_value = UserDetailsDTO(
            user_id=1,
            is_admin=True
        )
        mandal_storage = create_autospec(MandalStorageInterface)
        presenter = create_autospec(PresenterInterface)
        mandal_storage.is_mandal_stats_exists.return_value = True

        interactor = CreateOrUpdateMandalStatisticsInteractor(
            mandal_storage=mandal_storage,
            presenter=presenter
        )

        # Act
        interactor.create_or_update_mandal_statistics(
            user_id=user_id,
            for_date=for_date,
            total_confirmed=total_confirmed,
            total_recovered=total_recovered,
            total_deaths=total_deaths,
            mandal_id=mandal_id
        )

        # Assert
        mandal_storage.is_valid_mandal_id.assert_called_once_with(
            mandal_id=mandal_id
        )
        mandal_storage.is_mandal_stats_exists.assert_called_once_with(
            mandal_id=mandal_id, for_date=for_date
        )
        mandal_storage.update_mandal_statistics.assert_called_once_with(
            for_date=for_date,
            total_confirmed=total_confirmed,
            total_recovered=total_recovered,
            total_deaths=total_deaths,
            mandal_id=mandal_id
        )
