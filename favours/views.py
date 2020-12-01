from apps.listings.models import Post
from django.views.generic import ListView


class PostListView(ListView):
    # paginated list of posts
    model = Post
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
