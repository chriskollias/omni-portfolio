from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField()
    city = forms.TextInput()

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'city']