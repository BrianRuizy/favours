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
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
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
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    else request.method == 'DELETE':
        pass