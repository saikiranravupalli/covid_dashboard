from dataclasses import dataclass
from typing import List

from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \
    UserDetailsDTO, DomainJoinRequestDTO, PostDTO, PostReactionsCountDTO, \
    CommentDTO, PostCommentsCountDTO, CommentReactionsCountDTO, \
    CommentRepliesCountDTO, PostTagsDTO, TagDTO


@dataclass()
class DomainDetailsDTO:
    domain: DomainDTO
    domain_stats: DomainStatsDTO
    domain_experts: List[UserDetailsDTO]
    join_requests: List[DomainJoinRequestDTO]
    requested_users: List[UserDetailsDTO]
    user_id: int
    is_user_domain_expert: bool

@dataclass()
class CompletePostDetailsDTO:
    posts: List[PostDTO]
    post_reactions_count: List[PostReactionsCountDTO]
    comments: List[CommentDTO]
    comments_count: List[PostCommentsCountDTO]
    comment_reactions_count: List[CommentReactionsCountDTO]
    comment_replies_count: List[CommentRepliesCountDTO]
    post_tags: List[PostTagsDTO]
    tags: List[TagDTO]
    users: List[UserDetailsDTO]
