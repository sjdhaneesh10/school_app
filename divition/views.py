from django.shortcuts import render
from .models import Divition

# Create your views here.
def divition_view(request):
    divition=Divition.objects.all()
    div_tbh=['Class Name','Diviion Name',]
    divdic={
        'divition':divition,
        'div_tbh':div_tbh,
    }
    return render(request,'divition/divition.html',divdic)
