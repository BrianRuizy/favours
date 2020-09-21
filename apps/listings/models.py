from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from pygments import styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Sets where to redirect user after submitting a post
        return reverse('post-detail', kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        """ using pygments, mehod will create a highlighted
        and friendly representation of the code snippet. """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.title,
            linenos=linenos,
            full=True,
            **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Post, self).save(*args, **kwargs)
