from django.shortcuts import render
from .models import Teacher
from .forms import TeacherForm
from django.http import HttpResponseRedirect
# Create your views here.


def  teacher_view(request):
    teacher=Teacher.objects.all()
    table_head=['Teacher name','Class','Mob no','Address','DOB','Edit','Delete']
    dic = {
        'table_head':table_head,
        'teacher':teacher,
    }
    print(request.user)
    return render(request,'teacher/home.html',dic)


def add(request):
    if request.method == 'GET':

        add_form = TeacherForm()
        context = {
            'form':add_form,
            'url':'/teacher/add/'
        }
        return render(request,'teacher/add.html',context)

    if request.method == 'POST':
        add_form = TeacherForm(data=request.POST,files=request.FILES)
        err = add_form.errors
        if add_form.is_valid():
            add_form.save()
            return HttpResponseRedirect('/teacher/')
        else:
            add_form = TeacherForm()
            context = {
                'form':add_form,
                'url':'/teacher/add/',
                'error' : err
            }
            return render(request,'teacher/add.html',context)


def edit(request,id):
    details = Teacher.objects.get(pk=id)
    add_form = TeacherForm(data=request.POST or None,files=request.FILES or None,instance=details)
    if add_form.is_valid():
        add_form.save()
        return HttpResponseRedirect('/teacher/')
    else:
        context = {
            'form':add_form,
            'url':'/teacher/edit/'+str(id)+'/'
        }
        return render(request,'teacher/add.html',context)

def delete(request,id):
    details = Teacher.objects.get(pk=id)
    details.delete()
    return HttpResponseRedirect('/teacher/')

def details(request,id):
    details = Teacher.objects.get(pk=id)
    context = {
        'teacher':details
    }
    return render(request,'teacher/details.html',context)

