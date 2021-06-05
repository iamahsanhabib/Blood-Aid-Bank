from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'Statement'

urlpatterns = [
    path('tax/add/', views.addTax, name='add_tax'),
    path('tax/', views.showTax, name='show_tax'),
    path('tax/delete/<str:pk>', views.deleteTax, name='delete_tax'),
    path('financial/add/', views.addFinancial, name='add_financial'),
    path('financial/', views.show_financial, name='show_financial'),
    path('financial/delete/<str:pk>', views.delete_financial, name='delete_financial'),
    path('blood-donation/add/', views.add_blood_statment, name='add_bloodstatement'),
    path('blood-donation/delete/<str:pk>', views.delete_blood_statment, name='delete_bloodstatement'),
    path('blood-donation/', views.show_blood_statment, name='show_bloodstatement'),
    path('daily-donation/add/', views.add_blood_donation, name='add_blood_donation'),
    path('total-donation/add/', views.total_blood_donation, name='total_blood_donation'),
]