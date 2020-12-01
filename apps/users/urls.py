from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # used by social-media logins
    path('login/', views.MyLoginView.as_view(), name='account_login'),
    path('logout/', views.MyLogoutView.as_view(), name='account_logout'),
    path('signup/', views.MySignupView.as_view(), name='account_signup'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('account/password-reset/', views.MyPasswordResetView.as_view(), name='account_reset_password'),
    path('account/personal-info/', views.personal_info, name='account_personal_info'),
    path('user/<str:username>', views.user_profile(), name='user-posts'),
]

if settings.DEBUG:
    # FIXME: default profile image not appearing
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
