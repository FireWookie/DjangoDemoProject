from django.urls import path

from account import views

app_name = 'account'
urlpatterns = [
    path('auth/registration/', views.index, name='registration'),
    path('auth/login/', views.LoginMain.as_view(), name='login'),
]
