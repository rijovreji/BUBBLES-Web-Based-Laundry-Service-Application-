from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from User_Web.models import *


# Create your views here.

def Home(request):
    return render(request,'home.html')
def signin_signup(request):
    return render(request,'signin_signup.html')
def saveUser_Registration(request):
    if request.method=="POST":
        uname=request.POST.get('Username')
        email=request.POST.get('Email')
        pswd=request.POST.get('Password')
        conf_pswd=request.POST.get('Confirm_Password')
        obj=UserRegistration_db(username=uname,
                                email=email,
                                password=pswd,
                                conf_password=conf_pswd)
        if UserRegistration_db.objects.filter(username=uname).exists():
            return redirect(signin_signup)
        elif UserRegistration_db.objects.filter(email=email).exists():
            return redirect(signin_signup)
        else:
            obj.save()
            return redirect(signin_signup)

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        if UserRegistration_db.objects.filter(username=uname,password=pswd).exists():



            return redirect(Home)
        else:
            return redirect(signin_signup)
    else:
        return redirect(signin_signup)
def user_logout(request):
    request.session.pop('username', None)
    request.session.pop('password', None)
    return redirect(signin_signup)




















