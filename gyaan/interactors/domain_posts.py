from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.exceptions.exceptions import UserNotDomainMember, \
    DomainDoesNotExist, InvalidOffsetLength, InvalidLimitLength

class DomainPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_posts_wrapper(self, user_id: int, domain_id: int,
                                 offset: int, limit: int,
                                 presenter: PresenterInterface):
        try:
            domain_posts = self.get_domain_posts(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset,
                limit=limit
            )
        except DomainDoesNotExist:
            presenter.raise_domain_does_not_exist_exception()
        except UserNotDomainMember:
            presenter.raise_user_not_domain_member_exception()
        except InvalidOffsetLength:
            presenter.raise_exception_for_invalid_offset_length()
        except InvalidLimitLength:
            presenter.raise_exception_for_invalid_limit_length()
        else:
            return presenter.get_domain_posts_response(domain_posts)

    def get_domain_posts(self, user_id: int, domain_id: int,
                         offset: int, limit: int):

        # TODO: validate domain id
        self.storage.is_valid_domain_id(domain_id)

        # TODO: validate user
        is_user_following_domain = self.storage.is_user_following_domain(
            user_id=user_id, domain_id=domain_id)
        is_user_not_following_domain = not is_user_following_domain

        if is_user_not_following_domain:
            raise UserNotDomainMember()

        # TODO: validate offset and limit value
        self._validate_offset_and_limit_values(offset, limit)

        # TODO: check limit length
        is_limit_length_is_zero = limit == 0
        if is_limit_length_is_zero:
            limit = 15

        # TODO: get domain post ids
        post_ids = self.storage.get_domain_post_ids(domain_id=domain_id,
                                                    offset=offset,
                                                    limit=limit)

        # TODO: get domain posts
        from gyaan.interactors.get_posts import GetPostsInteractor
        get_posts_interactor = GetPostsInteractor(storage=self.storage)

        complete_post_details = \
            get_posts_interactor.get_posts(post_ids=post_ids)

        return complete_post_details

    @staticmethod
    def _validate_offset_and_limit_values(offset: int, limit: int):
        if offset < 0:
            raise InvalidOffsetLength
        if limit < 0:
            raise InvalidLimitLength
