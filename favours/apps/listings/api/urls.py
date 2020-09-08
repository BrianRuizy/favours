from django.urls import path

from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='api-post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='api-post-details'),
]