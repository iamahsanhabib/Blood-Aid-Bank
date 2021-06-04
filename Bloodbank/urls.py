from django.urls import path

app_name = 'BloodBank'
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
]