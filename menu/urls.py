
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home,name='home'),
    path('home/add/', add_meal,name='add_meal'),
    path('home/details/', meal_details,name='meal_details'),
    path('home/details/update', update_meal,name='update_meal'),
    path('home/details/delete', delete_meal,name='delete_meal'),
]
