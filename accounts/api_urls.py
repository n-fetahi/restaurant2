
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('signup/', sign_up,name='signup'),
    path('userinfo/', user_info,name='userinfo'),
    path('userinfo/updates/', update_user,name='update'),
    
]
