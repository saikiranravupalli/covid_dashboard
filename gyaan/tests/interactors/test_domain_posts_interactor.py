import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from gyaan.exceptions.exceptions import DomainDoesNotExist, \
    UserNotDomainMember
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.domain_posts import DomainPostsInteractor
from gyaan.interactors.get_posts import GetPostsInteractor
    
    
def test_get_domain_posts_interactor_with_invalid_domain_id_raises_exception():

    # Arrange
    invalid_domain_id = -1
    user_id = 1
    offset = 0
    limit = 10

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainPostsInteractor(storage=storage)

    storage.is_valid_domain_id.side_effect = DomainDoesNotExist
    presenter.raise_domain_does_not_exist_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_wrapper(
            user_id=user_id,
            domain_id=invalid_domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=invalid_domain_id)
    presenter.raise_domain_does_not_exist_exception.assert_called_once()

def test_get_domain_posts_interactor_with_user_not_domain_member_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 10

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainPostsInteractor(storage=storage)

    storage.is_user_following_domain.side_effect = UserNotDomainMember
    presenter.raise_user_not_domain_member_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    presenter.raise_user_not_domain_member_exception.assert_called_once()

def test_get_domain_posts_interactor_with_invalid_offset_length_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    offset = -1
    limit = 10

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainPostsInteractor(storage=storage)

    presenter.raise_exception_for_invalid_offset_length.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()

def test_get_domain_posts_interactor_with_invalid_limit_length_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = -1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainPostsInteractor(storage=storage)

    presenter.raise_exception_for_invalid_limit_length.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()

def test_get_domain_posts_interactor_with_valid_details_returns_post_details(
    complete_post_details):

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 10

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainPostsInteractor(storage=storage)

    storage.is_user_following_domain.return_value = True
    storage.get_domain_post_ids.return_value = [1, 2]

    # Act
    with patch.object(
        GetPostsInteractor, 'get_posts', return_value=complete_post_details):
        interactor.get_domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    storage.get_domain_post_ids.assert_called_once_with(
        domain_id=domain_id, offset=offset, limit=limit)
    presenter.get_domain_posts_response.assert_called_once_with(
        complete_post_details_dto=complete_post_details)

def test_get_domain_posts_interactor_with_limit_as_zero_returns_post_details(
    complete_post_details):

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 0

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainPostsInteractor(storage=storage)

    storage.is_user_following_domain.return_value = True
    storage.get_domain_post_ids.return_value = [1, 2]

    # Act
    with patch.object(
        GetPostsInteractor, 'get_posts', return_value=complete_post_details):
        interactor.get_domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_valid_domain_id.assert_called_once_with(domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    storage.get_domain_post_ids.assert_called_once_with(
        domain_id=domain_id, offset=offset, limit=15)
    presenter.get_domain_posts_response.assert_called_once_with(
        complete_post_details_dto=complete_post_details)
