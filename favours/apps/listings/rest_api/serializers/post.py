from rest_framework import serializers

from favours.apps.users.models import User
from favours.apps.listings.models import Category, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'username')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    author = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'description', 'category', 'author')
