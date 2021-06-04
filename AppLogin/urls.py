from django.urls import path

app_name = 'AppLogin'
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('change-profile/', views.change_user_profile, name='change_profile'),
    path('password/', views.change_user_password, name='change_password'),
    
]