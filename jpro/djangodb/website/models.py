from django.db import models
from datetime import *

# Create your models here

class User_Details(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)  