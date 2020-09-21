from rest_framework import generics

from apps.listings.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """ Reads all posted favours,
    or post a new favour if valid post request """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Read, update, or delete a specific posted favou """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
