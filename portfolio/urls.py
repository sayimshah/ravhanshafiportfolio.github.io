from unicodedata import name
from django.contrib import admin
from django.urls import path
from  portfolio.views import *  

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('resume', resume, name='resume'),
]