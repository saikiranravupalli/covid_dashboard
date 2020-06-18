from typing import List
from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.dtos import CompletePostDetailsDTO


class GetPostsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_wrapper(self, post_ids: List[int],
                          presenter: PresenterInterface):
        try:
            complete_post_details_dto = self.get_posts(post_ids)
        except InvalidPostIds as err:
            presenter.raise_exception_for_invalid_post_ids(err=err)
        else:
            return presenter.get_posts_response(complete_post_details_dto)

    def get_posts(self, post_ids: List[int]):

        # TODO: check unique post_ids
        post_ids = self._get_unique_post_ids(post_ids)

        # TODO: validate post_ids
        self._validate_post_ids(post_ids)

        # TODO: get user ids
        user_ids = self.storage.get_posts_user_ids(post_ids=post_ids)

        # TODO: get posts
        posts = self.storage.get_posts(post_ids=post_ids)

        # TODO: get users details
        users = self.storage.get_users_details(user_ids=user_ids)
    
        # TODO: get post tags
        post_tags, tags = self._get_post_tags(post_ids=post_ids)

        # TODO: get post reactions count
        post_reactions_count = self.storage.get_post_reactions_count(
            post_ids=post_ids)

        # TODO: get post comments count
        comments_count = self.storage.get_post_comments_count(
            post_ids=post_ids)

        # TODO: get post comment ids
        comment_ids = self._get_latest_comment_ids(post_ids)

        # TODO: get comment details
        comments = self.storage.get_comments(comment_ids=comment_ids)

        # TODO: get comments user_ids
        comment_user_ids = self.storage.get_comments_user_ids(
            comment_ids=comment_ids)

        # TODO: get comment users
        users += self.storage.get_users_details(user_ids=comment_user_ids)

        # TODO: get comment reactions count
        comment_reactions_count = self.storage.get_comment_reactions_count(
            comment_ids=comment_ids)

        # TODO: get comment replies count
        comment_replies_count = self.storage.get_replies_count(
            comment_ids=comment_ids)

        complete_post_details = CompletePostDetailsDTO(
            posts=posts,
            post_reactions_count=post_reactions_count,
            comments=comments,
            comments_count=comments_count,
            comment_reactions_count=comment_reactions_count,
            comment_replies_count=comment_replies_count,
            post_tags=post_tags,
            tags=tags,
            users=users
        )
        return complete_post_details


    def _validate_post_ids(self, post_ids):
        valid_post_ids = self.storage.get_valid_post_ids(post_ids=post_ids)

        invalid_post_ids = list(set(post_ids) - set(valid_post_ids))

        if invalid_post_ids:
            raise InvalidPostIds(invalid_post_ids)

    def _get_post_tags(self, post_ids: List[int]):
        post_tags = self.storage.get_post_tags(post_ids=post_ids)
        tag_ids = [post_dto.tag_id for post_dto in post_tags]
        tags = self.storage.get_tags(tag_ids=tag_ids)

        return post_tags, tags

    def _get_latest_comment_ids(self, post_ids: List[int]):
        comment_ids = []
        for post_id in post_ids:
            comment_ids += self.storage.get_comment_ids(
                post_id=post_id, no_of_comments=2
            )
        return comment_ids

    @staticmethod
    def _get_unique_post_ids(post_ids: List[int]):
        post_ids = list(dict.fromkeys(post_ids))
        return post_ids
