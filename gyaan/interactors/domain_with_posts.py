from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.exceptions.exceptions import UserNotDomainMember, \
    DomainDoesNotExist, InvalidOffsetLength, InvalidLimitLength
from gyaan.interactors.presenters.dtos import DomainWithPostsDetailsDTO

class DomainWithPostsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_with_posts_wrapper(self, user_id: int, domain_id: int,
                                      offset: int, limit: int,
                                      presenter: PresenterInterface):
        try:
            domain_with_posts_details = self.get_domain_with_posts(
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
            return presenter.get_domain_with_posts_response(
                domain_with_posts_details_dto=domain_with_posts_details)

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int):

        # TODO: get domain with posts
        from gyaan.interactors.domain_details import \
            DomainDetailsInteractor
        domain_details_interactor = DomainDetailsInteractor(
            storage=self.storage)
        domain_details = domain_details_interactor.get_domain_details(
            user_id=user_id, domain_id=domain_id)

        from gyaan.interactors.domain_posts import DomainPostsInteractor
        domain_posts_interactor = DomainPostsInteractor(
            storage=self.storage)
        domain_posts = domain_posts_interactor.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        complete_domain_details = DomainWithPostsDetailsDTO(
            domain_details=domain_details,
            domain_posts=domain_posts
        )
        return complete_domain_details
