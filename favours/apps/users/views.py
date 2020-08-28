from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView, LogoutView, PasswordResetView

from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


class MyLoginView(LoginView):
    template_name = 'allauth/login.html'


class MyLogoutView(LogoutView):
    template_name = 'allauth/logout.html'


class MySignupView(SignupView):
    template_name = 'allauth/signup.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'


@login_required
def profile(request):
    profile = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'profile_form': p_form
        }
    return render(request, 'profile.html', context=context)


@login_required
def account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('account')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': u_form
        }
    return render(request, 'account.html', context=context)


@login_required
def personal_info(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('account')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': u_form
        }
    return render(request, 'account/personal_info.html', context=context)
