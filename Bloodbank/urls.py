from django.urls import path

app_name = 'Bloodbank'
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
]