from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from Admin_Panel.models import *
from User_Web.models import *


# Create your views here.
def Base_admin(request):
    users=UserRegistration_db.objects.count()
    orders = Order_DB.objects.count()
    service = Serviece_DB.objects.count()

    return render(request, 'base.html',
                  {"users":users,"orders":orders,"service":service})


def Dashboard(request):
    return render(request, 'index.html')


def Add_Service_admin(request):
    return render(request, 'Add_Service_admin.html')


def Save_service(request):
    if request.method == "POST":
        S_name = request.POST.get('service_name')
        S_price = request.POST.get('price')
        S_short_dec = request.POST.get('short_description')
        S_description = request.POST.get('description')
        S_status = request.POST.get('status')
        S_img = request.FILES["service_image"]
        obj = Serviece_DB(service_name=S_name,
                          service_price=S_price,
                          service_short_desc=S_short_dec,
                          service_description=S_description,
                          service_status=S_status,
                          service_image=S_img)
        obj.save()
        return redirect(Add_Service_admin)


def View_Service_admin(request):
    services = Serviece_DB.objects.all()
    return render(request, 'View_Service_admin.html',
                  {'services': services})


def Edite_serviese(request, s_id):
    data = Serviece_DB.objects.get(id=s_id)
    return render(request, 'Edite_serviese.html',
                  {'data': data})


def update_servies(request, s_id):
    if request.method == "POST":
        S_name = request.POST.get('service_name')
        S_price = request.POST.get('price')
        S_short_dec = request.POST.get('short_description')
        S_description = request.POST.get('description')
        S_status = request.POST.get('status')

        try:
            img = request.FILES["service_image"]
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Serviece_DB.objects.get(id=s_id).service_image

        Serviece_DB.objects.filter(id=s_id).update(
            service_name=S_name,
            service_price=S_price,
            service_short_desc=S_short_dec,
            service_description=S_description,
            service_status=S_status,
            service_image=file
        )

        return redirect(View_Service_admin)
def delete_Service(request, s_id):
    service = Serviece_DB.objects.filter(id=s_id)
    service.delete()
    return redirect(View_Service_admin)
def view_user(request):
    users=UserRegistration_db.objects.all()
    return render(request, 'view_user.html',
                  {'users':users})
def view_order(request):
    data = Order_DB.objects.all().order_by('-id')
    return render(request, 'view_order.html', {'data': data})

def update_order_statues(request):
    return render(request, 'update_order_statues.html')
def view_Paid_orders(request):
    return render(request, 'view_Paid_orders.html')
def view_unpaid_orders(request):
    return render(request, 'view_unpaid_orders.html')
def login_admin(request):
    return render(request,'login_admin.html')
def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            data=authenticate(username=uname,password=pswd)
            if data is not None:
                login(request,data)
                request.session['username']=uname
                request.session['password']=pswd

                return redirect(Base_admin)
            else:
                return redirect(login_admin)

        else:
            return redirect(login_admin)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_admin)
def view_response(request):
    data=Contact_Db.objects.all()
    return render(request,'view_response.html',
                  {'data':data})






