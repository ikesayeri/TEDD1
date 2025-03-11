from django.urls import path
from .views import home, login_view, register_view, profile_view, messages_view, create_post_view, follow_unfollow, add_comment, get_comments, post_detail, like_post, dislike_post, search_view


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('messages/', messages_view, name='messages'),
    path('create/', create_post_view, name='create_post'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('profile/<str:username>/follow/', follow_unfollow, name='follow_unfollow'),
    path("create_post/", create_post_view, name="create_post"),
    path("post/<int:post_id>/comment/", add_comment, name="add_comment"),
    path("post/<int:post_id>/comments/", get_comments, name="get_comments"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path("post/<int:post_id>/like/", like_post, name="like_post"),
    path("post/<int:post_id>/dislike/", dislike_post, name="dislike_post"),
    path("search/", search_view, name="search"),
]
