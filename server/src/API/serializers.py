from django.contrib.auth.models import User, Group
from rest_framework import serializers
from src.models import Tweet, Follow


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content', 'author']

class UserFollowerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    class Meta:
        model = Follow
        fields = ['username','email']

    def get_username(self,obj):
        return obj.user.username

    def get_email(self,obj):
        return obj.user.email

class UserFollowsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    class Meta:
        model = Follow
        fields = ['username','email']

    def get_username(self,obj):
        return obj.follow_user.username

    def get_email(self,obj):
        return obj.follow_user.email