import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from gyaan.exceptions.exceptions import DomainDoesNotExist, \
    UserNotDomainMember
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.domain_with_posts import DomainWithPostsInteractor
from gyaan.interactors.domain_posts import DomainPostsInteractor
from gyaan.interactors.domain_details import DomainDetailsInteractor
    

@patch.object(DomainDetailsInteractor, 'get_domain_details')
@patch.object(DomainPostsInteractor, 'get_domain_posts')
def test_domain_with_posts_interactor_with_valid_details_returns_post_details(
    get_domain_posts_mock, get_domain_details_mock,
    complete_post_details, domain_details_dto, domain_with_posts_details):

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 10

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainWithPostsInteractor(storage=storage)

    get_domain_details_mock.return_value = domain_details_dto
    get_domain_posts_mock.return_value = complete_post_details

    # Act
    interactor.get_domain_with_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    # Assert
    presenter.get_domain_with_posts_response.assert_called_once_with(
        domain_with_posts_details_dto=domain_with_posts_details)
