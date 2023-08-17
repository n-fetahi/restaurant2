
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('menu/', all_menu,name='all_menu'),
    path('menu/<str:search_id>/', get_meal_by_ID,name='all_menu'),
    
]
