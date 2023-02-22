from django.urls import path
from . import views

app_name = 'Employee'

urlpatterns = [
    path('', views.showtable, name='Employee_data'), 
    path('', views.SaveData, name='Employee_data')
]