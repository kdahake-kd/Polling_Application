from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView as logout
)
# Create your views here.

class Login(LoginView):
    template_name='auth/login.html'
    allow_authenticate_user=False