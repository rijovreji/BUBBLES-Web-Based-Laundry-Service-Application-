from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from Admin_Panel.models import *


# Create your views here.
def Base_admin(request):
    return render(request, 'base.html')


def Dashboard(request):
    return render(request, 'index.html')


def Add_Service_admin(request):
    return render(request, 'Add_Service_admin.html')


def Save_service(request):
    if request.method == "POST":
        S_name = request.POST.get('service_name')
        S_price = request.POST.get('price')
        S_description = request.POST.get('description')
        S_status = request.POST.get('status')
        obj = Serviece_DB(service_name=S_name,
                          service_price=S_price,
                          service_description=S_description,
                          service_status=S_status)
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
        S_description = request.POST.get('description')
        S_status = request.POST.get('status')
        Serviece_DB.objects.filter(id=s_id).update(service_name=S_name,
                                                      service_price=S_price,
                                                      service_description=S_description,
                                                      service_status=S_status)
        return redirect(View_Service_admin)
def delete_Service(request, s_id):
    service = Serviece_DB.objects.filter(id=s_id)
    service.delete()
    return redirect(View_Service_admin)




