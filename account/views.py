from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from account.forms import LoginForm, UserRegisterForm


def index(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            form.add_error('email', "Пользователь с таким E-MAIL уже зарегестрирован!")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            ins = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password, email=email)
            ins.email = email
            ins.first_name = first_name
            ins.last_name = last_name
            ins.save()
            form.save_m2m()
            messages.success(request, 'Вы успешно зарегестрировались!')
            login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context = {'form': form}
    print(form.errors)
    return render(request, 'auth/registration/registration.html', context)


class LoginMain(LoginView):
    template_name = "auth/login/login.html"
    form_class = LoginForm
