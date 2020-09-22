from rest_framework import generics, permissions
from django.contrib.auth.models import User
from apps.api.permissions import IsOwnerOrReadOnly

from apps.listings.models import Post
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    """ Reads all posted favours,
    or post a new favour if valid post request """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Associates user with snippets
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Read, update, or delete a specific posted favou """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
