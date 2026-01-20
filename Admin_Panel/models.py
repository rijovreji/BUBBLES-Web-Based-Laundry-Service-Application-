from django.db import models
from User_Web.models import *


# Create your models here.
class Serviece_DB(models.Model):
    service_name=models.CharField(max_length=100,null=True,blank=True)
    service_price=models.IntegerField(null=True,blank=True)
    service_short_desc = models.TextField(max_length=100, null=True, blank=True)
    service_description=models.TextField(max_length=400,null=True,blank=True)
    service_status=models.CharField(max_length=100,null=True,blank=True)
    service_image = models.ImageField(upload_to="serviece_images", null=True, blank=True)
class Order_DB(models.Model):
    user = models.ForeignKey(
        UserRegistration_db,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    service = models.ForeignKey(
        Serviece_DB,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)

    pickup_address = models.TextField(max_length=300, null=True, blank=True)
    delivery_address = models.TextField(max_length=300, null=True, blank=True)
    customer_name=models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20, default="Pending")


