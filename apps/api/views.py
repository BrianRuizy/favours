from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.listings.models import Post
from .serializers import PostSerializer


# class PostList(generics.ListCreateAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter, )  # basic search functionality
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    """ Read all posted favours,
    or post a new favour if valid post request """
    if request.method == 'GET':
        all_posts = Post.objects.all()
        serializer = PostSerializer(all_posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view('GET', 'PUT', 'DELETE')
def post_detail(request, pk):
    """ Read, update, or delete a specific posted favour """
    try:
        specific_post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(specific_post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(specific_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        specific_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)