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
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')
        if password!=confirm_password:
            messages.info(request, "Password didnot match")
            return redirect('/auth/signup/')
        elif User.objects.filter(username=email).exists():
                messages.info(request, "Email already Taken")
                return redirect('/auth/signup/')
        else:
            myuser=User.objects.create_user(username=email , email=email , password=password)
            myuser.save()
            messages.success(request, "User is created please login")
            return redirect('/auth/login/')


    return render(request, 'signup.html')



def handlelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        myuser = authenticate(username= email , password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login success')
            return redirect("/")
        else:
            messages.error(request,'Incorrect Credentials')

    return render(request, 'login.html')



def handlelogout(request):
    logout(request)
    return render(request, 'login.html')