from django.urls import path

from . import views


urlpatterns = [
    path('api/posts/', views.posts_list),
    path('api/post/<int:pk>/', views.post_detail),
]