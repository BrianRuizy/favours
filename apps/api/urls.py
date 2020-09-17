from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('api/posts/', views.post_list, name='api-post-list'),
    path('api/posts/<int:pk>', views.post_detail, name='api-post-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)