from django.urls import path, include
from src.API.views import TweetListAPIView, TweetCreateView, UserTweetListAPIView, FollowListAPIView, FollowersListAPIView

urlpatterns = [
    path('',TweetListAPIView.as_view(),name='all_posts'),
    path('feed/new/',TweetCreateView.as_view(),name='post_create'),
    path('user/<str:username>/',UserTweetListAPIView.as_view(),name='user_posts'),
    path('user/<str:username>/followers/', FollowersListAPIView.as_view(),name='user_followers'),
    path('user/<str:username>/follows/', FollowListAPIView.as_view(),name='user_follows'),
]