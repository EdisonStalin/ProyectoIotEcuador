from django.db import models
import datetime #para la hora local

# Create your models here.

class User(models.Model):  
    uid = models.CharField(max_length=20)  
    uname = models.CharField(max_length=100)  
    uemail = models.EmailField()  
    upass = models.CharField(max_length=25)  
    class Meta:  
        db_table = "User"