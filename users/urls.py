from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register/', user_register_view, name='user-register'),
    path('logout/', user_logout_view, name='user-logout'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='user-login'),
]