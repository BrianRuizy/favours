from django.test import TestCase
from ..models import Post, Category


class PostTestCase(TestCase):
    def test_post(self):
        self.assertEquals(Post.objects.count(), 0)
        Post.objects.create(title='active', description='text')
        Post.objects.create(title='inactive', description='text')
        self.assertEquals(Post.objects.count(), 2)

        active_posts = Post.objects.active()
        self.assertEquals(active_posts.count(), 1)

        inactive_posts = Post.objects.inactive()
        self.assertEquals(inactive_posts.count(), 1)


class CategoryTestCase(TestCase):
    def test_category(self):
        self.assertEquals(Category.objects.count(), 0)
        Category.objects.create(name='name')
        self.assertEquals(Category.objects.count(), 1)
