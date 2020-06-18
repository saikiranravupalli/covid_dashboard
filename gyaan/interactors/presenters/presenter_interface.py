from abc import ABC
from abc import abstractmethod

from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.interactors.presenters.dtos import DomainDetailsDTO, \
    CompletePostDetailsDTO, DomainWithPostsDetailsDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_domain_does_not_exist_exception(self):
        pass

    @abstractmethod
    def raise_user_not_domain_member_exception(self):
        pass

    @abstractmethod
    def get_domain_details_response(
            self, domain_details_dto: DomainDetailsDTO):
        pass

    @abstractmethod
    def raise_exception_for_invalid_post_ids(self, err: InvalidPostIds):
        pass

    @abstractmethod
    def get_posts_response(self, 
                           complete_post_details_dto: CompletePostDetailsDTO):
        pass

    @abstractmethod
    def get_domain_posts_response(
        self, complete_post_details_dto: CompletePostDetailsDTO):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit_length(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset_length(self):
        pass

    @abstractmethod
    def get_domain_with_posts_response(
        self, domain_with_posts_details_dto: DomainWithPostsDetailsDTO):
        pass
