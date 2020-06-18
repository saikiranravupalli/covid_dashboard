from typing import List
from gyaan.exceptions.exceptions import UserNotDomainMember, \
    DomainDoesNotExist
from gyaan.interactors.presenters.dtos import DomainDetailsDTO
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface


class DomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(self, user_id: int, domain_id: int,
                                   presenter: PresenterInterface):
        try:
            domain_details_dto = self.get_domain_details(user_id=user_id,
                                                         domain_id=domain_id)
        except UserNotDomainMember:
            presenter.raise_user_not_domain_member_exception()
        except DomainDoesNotExist:
            presenter.raise_domain_does_not_exist_exception()
        else:
            return presenter.get_domain_details_response(domain_details_dto)

    def get_domain_details(self, user_id: int, domain_id: int):

        self.storage.is_valid_domain_id(domain_id)
        self.storage.is_user_following_domain(user_id=user_id,
                                              domain_id=domain_id)

        domain_dto = self.storage.get_domain_details(domain_id)
        domain_stats_dto = self.storage.get_domain_stats(domain_id)
        domain_expert_ids = self.storage.get_domain_expert_ids(domain_id)
        domain_experts = self.storage.get_users_details(domain_expert_ids)

        is_user_domain_expert, domain_join_requests, requested_user_details =\
            self._get_domain_experts_details(
                user_id=user_id,
                domain_id=domain_id,
                domain_expert_ids=domain_expert_ids)

        domain_details_dto = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=domain_experts,
            join_requests=domain_join_requests,
            requested_users=requested_user_details,
            is_user_domain_expert=is_user_domain_expert,
            user_id=user_id
        )
        return domain_details_dto

    def _get_domain_experts_details(self,
                                    user_id: int, 
                                    domain_id: int,
                                    domain_expert_ids: List[int]):

        is_user_domain_expert = user_id in domain_expert_ids
        domain_request_details = []
        requested_user_details = []

        if is_user_domain_expert:
            domain_request_details = \
                self.storage.get_domain_join_requests(domain_id)

        requested_user_ids = \
            [request_dto.user_id for request_dto in domain_request_details]

        if domain_request_details:
            requested_user_details = \
                self.storage.get_users_details(requested_user_ids)

        return is_user_domain_expert, domain_request_details, \
            requested_user_details
