from favours.apps.listings.models import Post
from .post import PostSerializer

post = Post.objects.create(title='first post', description='this is a test post')
print(PostSerializer(post).data)