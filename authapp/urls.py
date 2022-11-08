from django.contrib import admin
from django.urls import path
from  authapp.views import *  

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', handlelogin, name='handlelogin'),
    path('logout/', handlelogout, name='handlelogout'),
]