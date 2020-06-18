import pytest
from unittest.mock import create_autospec, call
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.get_posts import GetPostsInteractor

def test_get_posts_interactor_with_invalid_post_ids_raises_exception():
    # Arrange
    post_ids = [1, 2, 3, 4, 5]
    valid_post_ids = [1, 4, 5]
    invalid_post_ids = [2, 3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostsInteractor(storage=storage)
    storage.get_valid_post_ids.return_value = valid_post_ids
    presenter.raise_exception_for_invalid_post_ids.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_posts_wrapper(
            post_ids=post_ids,
            presenter=presenter
        )

    # Assert
    storage.get_valid_post_ids.assert_called_once_with(post_ids=post_ids)
    call_kwargs = presenter.raise_exception_for_invalid_post_ids\
        .call_args.kwargs['err']
    assert call_kwargs.args[0] == invalid_post_ids

def test_get_posts_interactor_with_valid_post_ids_returns_post_details_dto(
    user_details, post_details, post_tags, tags, post_reactions_count,
    post_comments_count, comments, comment_reactions_count,
    comment_replies_count, post_users, comment_users, complete_post_details):

    # Arrange
    post_ids = [1, 2]
    user_ids = [1, 2]
    comment_user_ids = [3, 4]
    tag_ids = [1, 2]
    comment_ids = [1, 2]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostsInteractor(storage=storage)

    storage.get_valid_post_ids.return_value = post_ids
    storage.get_posts_user_ids.return_value = user_ids
    storage.get_comments_user_ids.return_value = comment_user_ids
    storage.get_users_details.side_effect = [post_users, comment_users]
    storage.get_posts.return_value = post_details
    storage.get_post_tags.return_value = post_tags
    storage.get_tags.return_value = tags
    storage.get_post_reactions_count.return_value = post_reactions_count
    storage.get_post_comments_count.return_value = post_comments_count
    storage.get_comment_ids.side_effect = [[1], [2]]
    storage.get_comments.return_value = comments
    storage.get_comment_reactions_count.return_value = comment_reactions_count
    storage.get_replies_count.return_value = comment_replies_count

    # Act
    interactor.get_posts_wrapper(
        post_ids=post_ids,
        presenter=presenter
    )

    # Assert
    storage.get_valid_post_ids.assert_called_once_with(post_ids=post_ids)
    storage.get_posts_user_ids.assert_called_once_with(post_ids=post_ids)
    storage.get_users_details.assert_has_calls(
        [call(user_ids), call(comment_user_ids)]
    )
    storage.get_posts.assert_called_once_with(post_ids=post_ids)
    storage.get_post_tags.assert_called_once_with(post_ids=post_ids)
    storage.get_tags.assert_called_once_with(tag_ids=tag_ids)
    storage.get_post_reactions_count.assert_called_once_with(
        post_ids=post_ids)
    storage.get_post_comments_count.assert_called_once_with(
        post_ids=post_ids)
    storage.get_comment_ids.assert_has_calls(
        [call(post_id=1, no_of_comments=2), call(post_id=2, no_of_comments=2)]
    )
    storage.get_comments.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comments_user_ids.assert_called_once_with(
        comment_ids=comment_ids)
    storage.get_comment_reactions_count.assert_called_once_with(
        comment_ids=comment_ids)
    storage.get_replies_count.assert_called_once_with(comment_ids=comment_ids)
    presenter.get_posts_response.assert_called_once_with(
        complete_post_details_dto=complete_post_details
    )
