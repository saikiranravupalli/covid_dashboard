import datetime
from dataclasses import dataclass
from typing import List


@dataclass()
class DomainDTO:
    domain_id: int
    name: str
    description: str

@dataclass()
class DomainStatsDTO:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int

@dataclass()
class UserDetailsDTO:
    user_id: int
    name: str
    profile_pic_url: str

@dataclass()
class DomainJoinRequestDTO:
    request_id: int
    user_id: int

@dataclass()
class PostDTO:
    post_id: int
    post_content: str
    title: str
    posted_by_id: int
    posted_at: datetime.datetime

@dataclass()
class TagDTO:
    tag_id: int
    name: str

@dataclass()
class PostTagsDTO:
    post_id: int
    tag_id: int

@dataclass()
class PostReactionsCountDTO:
    post_id: int
    post_reactions_count: int

@dataclass()
class PostCommentsCountDTO:
    post_id: int
    post_comments_count: int

@dataclass()
class CommentDTO:
    comment_id: int
    comment_content: str
    commented_at: datetime.datetime
    post_id: int
    commented_by_id: int

@dataclass()
class CommentReactionsCountDTO:
    comment_id: int
    comment_reactions_count: int

@dataclass()
class CommentRepliesCountDTO:
    comment_id: int
    comment_replies_count: int
