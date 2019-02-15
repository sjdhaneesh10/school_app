from django.db import models
import datetime

# Create your models here.
from divition.models import Divition


class Student(models.Model):
    Name=models.CharField(max_length=20)
    #Class=models.ForeignKey()
    Divition=models.ForeignKey(Divition, on_delete=models.CASCADE)
    Address= models.TextField(max_length=100)
    DOB=models.DateField(max_length=8)

    def __str__(self):
        return self.Name

