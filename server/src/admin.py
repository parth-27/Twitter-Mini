from django.contrib import admin
from .models import Tweet, Follow, Profile

# Register your models here.

admin.site.register(Tweet)
admin.site.register(Follow)
admin.site.register(Profile)