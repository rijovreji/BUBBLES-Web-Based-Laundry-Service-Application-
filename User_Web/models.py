from django.db import models

# Create your models here.
class UserRegistration_db(models.Model):
    username=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    conf_password=models.CharField(max_length=50,null=True,blank=True)











