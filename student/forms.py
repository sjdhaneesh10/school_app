from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'DOB': forms.DateInput(attrs={'type':'date'}),
        }
