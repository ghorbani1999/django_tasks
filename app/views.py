from django.shortcuts import render , redirect
from app import models
from django.http import HttpResponse
from .forms import taskform
from django.contrib import messages


def list_tasks(request):
    tasks_objects = models.tasks.objects.all()
    count = models.tasks.objects.count()
    contex = {'tasks_objects':tasks_objects ,
    'count':count,
    }
    return render(request,'list.html',contex)


def show_task(request,id):
    contex = {'id' : id }
    return render(request,'show_task.html',contex)


def edit_task(request,id):
    return render(request,'edit_task.html')


def dashboard(request):
    return render(request,'dashboard.html')  


def create_task(request):
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'وظیفه ی جدید در سیستم ثبت شد')
            return redirect('list')
        else:
            messages.error(request, 'validation failded')
            return redirect('list')   
    if request.method == 'GET':
        return render(request,'create_task.html')
# Create your views here.
