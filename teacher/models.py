from django.db import models
import datetime

# Create your models here.
from divition.models import Divition


class Teacher(models.Model):
    Teacher_name=models.CharField(max_length=20)
    Class=models.ForeignKey(Divition,on_delete=models.CASCADE)
    Mob_no=models.CharField(max_length=10)
    Address=models.TextField(max_length=100)
    DOB=models.DateField()

    def __str__(self):
        return self.Teacher_name


