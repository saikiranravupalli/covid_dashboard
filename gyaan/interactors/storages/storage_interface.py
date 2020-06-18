from abc import ABC
from abc import abstractmethod
from typing import List

from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \
    UserDetailsDTO, DomainJoinRequestDTO, PostTagsDTO, TagDTO, CommentDTO, \
    CommentReactionsCountDTO, CommentRepliesCountDTO, PostDTO, \
    PostReactionsCountDTO, PostCommentsCountDTO


class StorageInterface(ABC):

    @abstractmethod
    def is_valid_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def get_domain_details(self, domain_id: int) -> DomainDTO:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatsDTO:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> List[UserDetailsDTO]:
        pass

    @abstractmethod
    def is_user_following_domain(self, domain_id: int, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_join_requests(self, domain_id: int) -> \
            List[DomainJoinRequestDTO]:
        pass

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_posts(self, post_ids: List[int]) -> List[PostDTO]:
        pass

    @abstractmethod
    def get_posts_user_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_post_reactions_count(self, post_ids: List[int]) -> \
        List[PostReactionsCountDTO]:
        pass

    @abstractmethod
    def get_post_comments_count(self, post_ids: List[int]) -> \
        List[PostCommentsCountDTO]:
        pass

    @abstractmethod
    def get_comments_user_ids(self, comment_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_post_tags(self, post_ids: List[int]) -> List[PostTagsDTO]:
        pass

    @abstractmethod
    def get_tags(self, tag_ids: List[int]) -> List[TagDTO]:
        pass

    @abstractmethod
    def get_comment_ids(self, post_id: int, no_of_comments: int) -> List[int]:
        pass

    @abstractmethod
    def get_comments(self, comment_ids: List[int]) -> List[CommentDTO]:
        pass

    @abstractmethod
    def get_comment_reactions_count(self, comment_ids: List[int]) -> \
        List[CommentReactionsCountDTO]:
        pass

    @abstractmethod
    def get_replies_count(self, comment_ids: List[int]) -> \
        List[CommentRepliesCountDTO]:
        pass
