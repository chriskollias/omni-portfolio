from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from portfolio.models import Portfolio

def user_register_view(request, *args, **kwargs):
    '''
    base_form is just for django's default User model, UserProfile form includes the additional fields we are asking for
    '''

    if request.method == 'POST':
        base_form = UserCreationForm(request.POST)
        user_profile_form = UserRegistrationForm(request.POST)
        if base_form.is_valid() and user_profile_form.is_valid():
            user = base_form.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user.first_name = user_profile_form.cleaned_data['first_name']
            user.last_name = user_profile_form.cleaned_data['last_name']
            user.email = user_profile_form.cleaned_data['email']
            user.save()
            user_profile.save()
            new_portfolio = Portfolio(user_profile=user_profile)
            new_portfolio.save()
            messages.success(request, "Account created successfully! You may now log in.")
            return redirect(reverse('user-login'))
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'users/registration.html', {'base_form': base_form, 'user_profile_form': user_profile_form})

    base_form = UserCreationForm()
    user_profile_form = UserRegistrationForm()
    return render(request, 'users/registration.html',  {'base_form': base_form, 'user_profile_form': user_profile_form})


def user_logout_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, "You have successfully logged in.")
    return redirect(reverse('landing-page'))


def user_login_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(reverse('landing-page'))
