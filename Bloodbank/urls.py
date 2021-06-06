from django.urls import path

app_name = 'Bloodbank'
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Donor_Registration/', views.addDonor, name = 'addDonor'),
    path('donor/', views.show_Donor, name = 'show_donor'),
    path('donor/search/', views.search_donor, name = 'search_donor'),
    path('donor/details/<str:pk>/', views.show_Donor_Details, name = 'details_donor'),
    path('donor/update/<str:pk>/', views.update_Donor_Details, name = 'update_donor'),
    path('donor/delete/<str:pk>/', views.delete_donor, name = 'delete_donor'),

    path('Member/', views.showMember, name = 'member'),
    path('Member/Add/', views.add_member, name = 'add_member'),
    path('Member/profile/Update/<str:pk>/', views.update_member_profile, name = 'update_member_profile'),
    path('Member/Details/<str:pk>/', views.detailsMember, name = 'details_member'),

    path('Registration/', views.addMember, name = 'addMember'),
    path('Application/List/', views.show_application_list, name = 'show_application_list'),
    path('Application/List/Details/<str:pk>/', views.show_application_details, name = 'show_application_details'),
    path('Application/List/Delete/<str:pk>/', views.delete_application_list, name = 'delete_application_list'),

    path('Blood_Booking/', views.bookBlood, name = 'booking'),
    path('Blood_Booking/list', views.show_booking_list, name = 'show_booking_list'),
    path('Blood_Booking/list/<str:pk>/', views.show_booking_details, name = 'show_booking_details'),
    path('Blood_Booking/list/delete/<str:pk>/', views.delete_booking, name = 'delete_booking'),

    path('About/', views.showAbout, name = 'about'),
]