from django.db import models
import datetime

# Create your models here.
class Divition(models.Model):
    Class_Name=models.CharField(max_length=5, help_text='Type number between 1 to 10')
    Divition_Name=models.CharField(max_length=5)

    def __str__(self):
        return self.Class_Name + self.Divition_Name
