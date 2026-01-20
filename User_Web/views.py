from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from User_Web.models import *
from Admin_Panel.models import *

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
        # if UserRegistration_db.objects.filter(username=uname,password=pswd).exists():
        #
        #
        #
        #     return redirect(Home)
        if UserRegistration_db.objects.filter(username=uname, password=pswd).exists():
            user = UserRegistration_db.objects.get(username=uname, password=pswd)

            request.session['user_id'] = user.id  # ✅ ADD
            request.session['username'] = user.username  # ✅ ADD (optional)

            return redirect(Home)
# ============================================================
        else:
            return redirect(signin_signup)
    else:
        return redirect(signin_signup)


def user_logout(request):
    request.session.pop('username', None)
    request.session.pop('password', None)
    return redirect(signin_signup)

def Save_Contact(request):
    if request.method=="POST":
        Contact_name=request.POST.get('name')
        Contact_email=request.POST.get('email')
        Contact_message=request.POST.get('message')
        obj=Contact_Db(contact_name=Contact_name,
                       contact_email=Contact_email,
                       contact_message=Contact_message)
        obj.save()
        return redirect(Home)
def service_user(request):
    data=Serviece_DB.objects.all()
    return render(request,'service_user.html',
                  {'data':data})

def book_order(request):



    data = Serviece_DB.objects.filter(service_status="Active")
    return render(request, 'book_order.html', {'data': data})

# def save_order(request):
#     if request.method == "POST":
#         customer_name=request.POST.get('customer_name')
#         service_id = request.POST.get('service_id')
#         pickup_date = request.POST.get('pickup_date')
#         pickup_time = request.POST.get('pickup_time')
#         pickup_address = request.POST.get('pickup_address')
#         delivery_address = request.POST.get('delivery_address')
#
#         # existing line (kept)
#         service_obj = Serviece_DB.objects.get(id=service_id)
#
#         # order create (completed, not restructured)
#         Order_DB.objects.create(
#             customer_name=customer_name,
#             service=service_obj,                       # FIX 2: correct FK
#             pickup_date=pickup_date,
#             pickup_time=pickup_time,
#             pickup_address=pickup_address,
#             delivery_address=delivery_address
#         )
#
#         return redirect(Home)
def save_order(request):
    if request.method == "POST":

        customer_name = request.POST.get('customer_name')
        service_id = request.POST.get('service_id')
        pickup_date = request.POST.get('pickup_date')
        pickup_time = request.POST.get('pickup_time')
        pickup_address = request.POST.get('pickup_address')
        delivery_address = request.POST.get('delivery_address')

        service_obj = Serviece_DB.objects.get(id=service_id)

        # ✅ get logged-in user
        user_id = request.session.get('user_id')
        user_obj = UserRegistration_db.objects.get(id=user_id)

        Order_DB.objects.create(
            user=user_obj,                  # ✅ FIX
            customer_name=customer_name,
            service=service_obj,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            pickup_address=pickup_address,
            delivery_address=delivery_address
        )

        return redirect('my_orders')
def my_orders(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect(signin_signup)

    orders = Order_DB.objects.filter(user_id=user_id)

    return render(request, 'myorder.html', {'orders': orders})
def service_detail(request, s_id):
    service = Serviece_DB.objects.get(id=s_id)
    return render(request, 'service_detail.html', {'service': service})





















