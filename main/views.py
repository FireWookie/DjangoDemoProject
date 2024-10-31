from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


@login_required(login_url="")
def portal(request):
    return render(request, 'main/portal/index.html')


def index(request):
    return render(request, 'index.html')