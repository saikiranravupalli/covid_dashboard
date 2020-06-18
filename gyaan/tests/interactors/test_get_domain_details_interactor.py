import pytest
from unittest.mock import create_autospec, call
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from gyaan.exceptions.exceptions import DomainDoesNotExist, \
    UserNotDomainMember
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.domain_details import DomainDetailsInteractor
    
    
def test_get_domain_details_interactor_with_invalid_domain_id_raises_exception():

    # Arrange
    invalid_domain_id = -1
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainDetailsInteractor(storage=storage)

    storage.is_valid_domain_id.side_effect = DomainDoesNotExist
    presenter.raise_domain_does_not_exist_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_details_wrapper(
            user_id=user_id,
            domain_id=invalid_domain_id,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=invalid_domain_id)
    presenter.raise_domain_does_not_exist_exception.assert_called_once()

def test_get_domain_details_interactor_with_user_not_domain_member_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainDetailsInteractor(storage=storage)

    storage.is_user_following_domain.side_effect = UserNotDomainMember
    presenter.raise_user_not_domain_member_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_details_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    presenter.raise_user_not_domain_member_exception.assert_called_once()

def test_get_domain_details_interactor_with_valid_details_returns_domain_dto(
    domain_details_dto, domain_dto, domain_stats_dto, domain_experts):

    # Arrange
    domain_id = 1
    user_id = 1
    domain_expert_ids = [2,3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainDetailsInteractor(storage=storage)

    storage.is_valid_domain_id.return_value = None
    storage.is_user_following_domain.return_value = True
    storage.get_domain_details.return_value = domain_dto
    storage.get_domain_stats.return_value = domain_stats_dto
    storage.get_domain_expert_ids.return_value = domain_expert_ids
    storage.get_users_details.return_value = domain_experts

    # Act
    interactor.get_domain_details_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        presenter=presenter
    )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    storage.get_domain_details.assert_called_once_with(domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id)
    storage.get_users_details.assert_called_once_with(domain_expert_ids)
    presenter.get_domain_details_response.assert_called_once_with(
        domain_details_dto)

def test_get_domain_details_interactor_with_user_as_domain_expert_returns_domain_dto(
    expert_user_domain_details_dto, domain_dto, domain_stats_dto,
    join_requests, requested_user_details, user_with_domain_experts):

    # Arrange
    domain_id = 1
    user_id = 1
    domain_expert_ids = [1,2,3]
    requested_user_ids = [4,5]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainDetailsInteractor(storage=storage)

    storage.is_valid_domain_id.return_value = None
    storage.is_user_following_domain.return_value = True
    storage.get_domain_details.return_value = domain_dto
    storage.get_domain_stats.return_value = domain_stats_dto
    storage.get_domain_expert_ids.return_value = domain_expert_ids
    storage.get_users_details.side_effect = [
        user_with_domain_experts,
        requested_user_details
    ]
    storage.get_domain_join_requests.return_value = join_requests

    # Act
    interactor.get_domain_details_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        presenter=presenter
    )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    storage.get_domain_details.assert_called_once_with(domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id)
    storage.get_users_details.assert_has_calls(
        [call(domain_expert_ids), call(requested_user_ids)]
    )
    presenter.get_domain_details_response.assert_called_once_with(
        expert_user_domain_details_dto)
