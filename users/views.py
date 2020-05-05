from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def user_register_view(request, *args, **kwargs):

    if request.method == 'POST':
        # base_form is just for django's default User model, UserProfile form includes the additional fields we are asking for
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
            return redirect(reverse('landing-page'))
        else:
            print('Send messages with signup errors here')

    base_form = UserCreationForm()
    user_profile_form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'base_form': base_form, 'user_profile_form': user_profile_form})

