from src.models import Tweet, Profile, Follow
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.contrib.auth.models import User
from .serializers import TweetSerializer, UserFollowsSerializer, UserFollowerSerializer

class TweetListAPIView(ListAPIView, LoginRequiredMixin):
    template_name = 'src/home.html'
    serializer_class = TweetSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        followed_users = Follow.objects.filter(user=user)
        followed_users_id = [obj.pk for obj in followed_users]

        return Tweet.objects.filter(author__in=followed_users_id).order_by('-date_posted')

class UserTweetListAPIView(ListAPIView, LoginRequiredMixin):
    serializer_class = TweetSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        try:
            user_obj = User.objects.get(username=username)
            return Tweet.objects.filter(author=user_obj).order_by('-date_posted')
        except:
            return []

class TweetCreateView(LoginRequiredMixin, GenericAPIView):

    def post(self,request):
        author = self.request.user
        content = self.request.data.get('content')

        obj = Tweet.objects.create(author=author,content=content)

        return Response(data='Successfully Created',status=status.HTTP_201_CREATED)

class FollowListAPIView(LoginRequiredMixin, ListAPIView):
    serializer_class = UserFollowsSerializer
    def get_queryset(self):
        username = self.kwargs.get('username')
        try:
            user = User.objects.get(username=username)
            return Follow.objects.filter(user=user).order_by('-date')
        except:
            return []


class FollowersListAPIView(LoginRequiredMixin, ListAPIView):
    serializer_class = UserFollowerSerializer
    def get_queryset(self):
        username = self.kwargs.get('username')
        try:
            user = User.objects.get(username=username)
            return Follow.objects.filter(follow_user=user).order_by('-date')
        except:
            return []

