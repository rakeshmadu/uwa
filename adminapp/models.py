from django.db import models
import datetime
# Create your models here.

class Reg(models.Model):
    GEND= (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')        
    )
    name = models.CharField(max_length = 50)
    age = models.CharField(max_length = 50)
    phonenumber = models.CharField(max_length = 50)
    Email = models.EmailField(default = "@gmail.com")
    gender = models.CharField(max_length = 50,choices = GEND)
    password= models.CharField(max_length = 50)
