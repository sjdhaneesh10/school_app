from django import forms
from django.forms import ModelForm
from .models import Teacher

class TeacherForm(ModelForm):
    
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'DOB': forms.DateInput(attrs={'type':'date'}),
        }
        widgets = {
            'Mob_no': forms.DateInput(attrs={'type':'text'}),
            
        }
        