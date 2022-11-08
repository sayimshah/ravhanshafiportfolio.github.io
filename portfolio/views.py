import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,login,logout
from .models import *

from django.contrib.auth.decorators import login_required
from itertools import chain

from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')


def resume(request):
    
    return render(request, 'resume.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('number')
        description = request.POST.get('message')

        query = Contacts.objects.create(name=name,email=email,phonenumber=phonenumber,description=description)
        query.save()

        messages.success(request, "Message Sent successfully!")
        return redirect('/contact')
    return render(request, 'contact.html')