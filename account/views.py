from django.contrib.auth.views import LoginView
from django.shortcuts import render

from account.forms import LoginForm


def index(request):
    return render(request, 'auth/registration/registration.html')


class LoginMain(LoginView):
    template_name = "auth/login/login.html"
    form_class = LoginForm
