from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path('portal', views.portal, name='portal'),
    path('', views.index, name='index'),
]
