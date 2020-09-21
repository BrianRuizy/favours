from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('api/posts/', views.PostList.as_view()),
    path('api/posts/<int:pk>', views.PostDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)