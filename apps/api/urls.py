from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)