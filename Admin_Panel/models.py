from django.db import models

# Create your models here.
class Serviece_DB(models.Model):
    service_name=models.CharField(max_length=100,null=True,blank=True)
    service_price=models.IntegerField(null=True,blank=True)
    service_description=models.TextField(max_length=400,null=True,blank=True)
    service_status=models.CharField(max_length=100,null=True,blank=True)



