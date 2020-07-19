from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView, LogoutView, PasswordResetView


from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


class MyLoginView(LoginView):
    template_name = 'allauth/login.html'


class MyLogoutView(LogoutView):
    template_name = 'allauth/logout.html'


class MySignupView(SignupView):
    template_name = 'allauth/signup.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'allauth/password_reset.html'


@login_required
def profile(request):
    profile = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
        
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, 'users/profile.html', context=context)