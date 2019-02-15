from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import HttpResponseRedirect


# Create your views here.
def student_view(request):
    student=Student.objects.all()
    student_tbh=['Name','Divition','Address','D.O.B','Edit','Delete']
    student_dic = {
        'student_tbh':student_tbh,
        'student':student,
        
    }

    return render(request,'student/student.html',student_dic)

def details(request,id):
    details = Student.objects.get(pk=id)
    context = {
        'student':details
    }
    return render(request,'student/stdetails.html',context)

def delete(request,id):
    details = Student.objects.get(pk=id)
    details.delete()
    return HttpResponseRedirect('/student/')

def edit(request,id):
    details = Student.objects.get(pk=id)
    
    add_form = StudentForm(data=request.POST or None,files=request.FILES or None,instance=details)
    if add_form.is_valid():
        add_form.save()
        return HttpResponseRedirect('/student/')
    else:
        add_form = StudentForm(instance=details)
        context = {
            'form':add_form,
            'url':'/student/edit/'+str(id)+'/'
        }
        return render(request,'student/add.html',context)




def add(request):
    if request.method == 'GET':

        add_form = StudentForm()
        context = {
            'form':add_form,
            'url':'/student/add/'
        }
        return render(request,'student/add.html',context)

    if request.method == 'POST':
        add_form = StudentForm(data=request.POST,files=request.FILES)
        err = add_form.errors
        if add_form.is_valid():
            add_form.save()
            return HttpResponseRedirect('/student/')
        else:
            add_form = StudentForm()
            context = {
                'form':add_form,
                'url':'/student/add/',
                'error' : err
            }
            return render(request,'student/add.html',context)