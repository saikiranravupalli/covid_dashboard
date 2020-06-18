import datetime
import pytest
from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \
    UserDetailsDTO, DomainJoinRequestDTO, PostDTO, PostTagsDTO, TagDTO, \
    PostReactionsCountDTO, PostCommentsCountDTO, CommentDTO, \
    CommentRepliesCountDTO, CommentReactionsCountDTO
from gyaan.interactors.presenters.dtos import CompletePostDetailsDTO
from gyaan.interactors.presenters.dtos import DomainDetailsDTO, \
    CompletePostDetailsDTO, DomainWithPostsDetailsDTO

@pytest.fixture
def domain_dto():
    domain_dto = DomainDTO(
        domain_id=1,
        name='Domain 1',
        description=""
    )
    return domain_dto

@pytest.fixture
def domain_stats_dto():
    domain_stats_dto = DomainStatsDTO(
        domain_id=1,
        followers_count=5,
        posts_count=10,
        bookmarked_count=10,
    )
    return domain_stats_dto

@pytest.fixture
def domain_experts():
    domain_experts = [
        UserDetailsDTO(
            user_id=2,
            name='user_2',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=3,
            name='user_3',
            profile_pic_url='' 
        )
    ]
    return domain_experts

@pytest.fixture
def user_with_domain_experts():
    domain_experts = [
        UserDetailsDTO(
            user_id=1,
            name='user_1',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=2,
            name='user_2',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=3,
            name='user_3',
            profile_pic_url='' 
        )
    ]
    return domain_experts

@pytest.fixture
def requested_user_details():
    requested_user_details = [
        UserDetailsDTO(
            user_id=4,
            name='user_4',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=5,
            name='user_5',
            profile_pic_url='' 
        )
    ]
    return requested_user_details

@pytest.fixture
def join_requests():
    join_requests = [
        DomainJoinRequestDTO(
            request_id=1,
            user_id=4
        ),
        DomainJoinRequestDTO(
            request_id=2,
            user_id=5
        )
    ]
    return join_requests

@pytest.fixture
def domain_details_dto(domain_dto, domain_stats_dto,
                       domain_experts):
    domain_details_dto = DomainDetailsDTO(
        domain=domain_dto,
        domain_stats=domain_stats_dto,
        domain_experts=domain_experts,
        join_requests=[],
        requested_users=[],
        user_id=1,
        is_user_domain_expert=False
    )
    return domain_details_dto

@pytest.fixture
def expert_user_domain_details_dto(domain_dto, domain_stats_dto,
                                   join_requests, user_with_domain_experts,
                                   requested_user_details):
    domain_details_dto = DomainDetailsDTO(
        domain=domain_dto,
        domain_stats=domain_stats_dto,
        domain_experts=user_with_domain_experts,
        join_requests=join_requests,
        requested_users=requested_user_details,
        user_id=1,
        is_user_domain_expert=True
    )
    return domain_details_dto

@pytest.fixture
def user_details():
    user_details = [
        UserDetailsDTO(
            user_id=1,
            name='user_1',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=2,
            name='user_2',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=3,
            name='user_3',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=4,
            name='user_4',
            profile_pic_url='' 
        )
    ]
    return user_details

@pytest.fixture
def post_users():
    post_users = [
        UserDetailsDTO(
            user_id=1,
            name='user_1',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=2,
            name='user_2',
            profile_pic_url='' 
        )
    ]
    return post_users

@pytest.fixture
def comment_users():
    comment_users = [
        UserDetailsDTO(
            user_id=3,
            name='user_3',
            profile_pic_url='' 
        ),
        UserDetailsDTO(
            user_id=4,
            name='user_4',
            profile_pic_url='' 
        )
    ]
    return comment_users

@pytest.fixture
def post_details():
    post_details = [
        PostDTO(
            post_id=1,
            title='POST 1',
            posted_by_id=1,
            posted_at=datetime.datetime.now(),
            post_content='post_1 content'
        ),
        PostDTO(
            post_id=2,
            title='POST 2',
            posted_by_id=2,
            posted_at=datetime.datetime.now(),
            post_content='post_1 content'
        )
    ]
    return post_details

@pytest.fixture
def post_tags():
    post_tags = [
        PostTagsDTO(
            post_id=1,
            tag_id=1
        ),
        PostTagsDTO(
            post_id=2,
            tag_id=2
        )
    ]
    return post_tags

@pytest.fixture
def tags():
    tags = [
        TagDTO(
            tag_id=1,
            name='tag_1'
        ),
        TagDTO(
            tag_id=2,
            name='tag_2'
        )
    ]
    return tags

@pytest.fixture
def post_reactions_count():
    post_reactions_count = [
        PostReactionsCountDTO(
            post_id=1,
            post_reactions_count=30
        ),
        PostReactionsCountDTO(
            post_id=2,
            post_reactions_count=50
        )
    ]
    return post_reactions_count

@pytest.fixture
def post_comments_count():
    post_comments_count = [
        PostCommentsCountDTO(
            post_id=1,
            post_comments_count=1
        ),
        PostCommentsCountDTO(
            post_id=2,
            post_comments_count=1
        )
    ]
    post_comments_count

@pytest.fixture
def comments():
    comments = [
        CommentDTO(
            comment_id=1,
            comment_content='comment 1',
            commented_at=datetime.datetime.now(),
            post_id=1,
            commented_by_id=3
        ),
        CommentDTO(
            comment_id=2,
            comment_content='comment 2',
            commented_at=datetime.datetime.now(),
            post_id=2,
            commented_by_id=4
        )
    ]
    return comments

@pytest.fixture
def comment_replies_count():
    comment_replies_count = [
        CommentRepliesCountDTO(
            comment_id=1,
            comment_replies_count=2
        ),
        CommentRepliesCountDTO(
            comment_id=2,
            comment_replies_count=2
        )
    ]
    return comment_replies_count

@pytest.fixture
def comment_reactions_count():
    comment_reactions_count = [
        CommentReactionsCountDTO(
            comment_id=1,
            comment_reactions_count=20
        ),
        CommentReactionsCountDTO(
            comment_id=2,
            comment_reactions_count=20
        )
    ]
    return comment_reactions_count

@pytest.fixture
def complete_post_details(post_details,
                          post_reactions_count,
                          comments,
                          post_comments_count,
                          comment_reactions_count,
                          comment_replies_count,
                          post_tags,
                          tags,
                          user_details):
    complete_post_details = CompletePostDetailsDTO(
        posts=post_details,
        post_reactions_count=post_reactions_count,
        comments=comments,
        comments_count=post_comments_count,
        comment_reactions_count=comment_reactions_count,
        comment_replies_count=comment_replies_count,
        post_tags=post_tags,
        tags=tags,
        users=user_details
    )
    return complete_post_details

@pytest.fixture
def domain_with_posts_details(complete_post_details, domain_details_dto):
    domain_with_posts_details = DomainWithPostsDetailsDTO(
        domain_details=domain_details_dto,
        domain_posts=complete_post_details
    )
    return domain_with_posts_details