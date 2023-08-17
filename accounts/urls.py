
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', redirect_login,name='index'),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
]
