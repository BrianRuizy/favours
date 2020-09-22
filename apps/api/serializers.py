from rest_framework import serializers

from apps.users.models import User
from apps.listings.models import Category, Post


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Post.objects.all()
        )

    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'pk',
            'email',
            'first_name',
            'last_name',
            'username', 
            'posts'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'pk',
            'title',
            'description',
            'price',
            'date_posted',
            'category',
            'owner',
        ]
