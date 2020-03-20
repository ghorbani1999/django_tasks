from django.shortcuts import render
from app import models

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
# Create your views here.
