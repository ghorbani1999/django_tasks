from django.shortcuts import render , redirect , get_object_or_404  
from app import models                      
from django.http import HttpResponse
from .forms import taskform
from django.contrib import messages
from django.core.paginator import Paginator



def list_tasks(request):
    paginator = Paginator(models.tasks.objects.all(),4)
    current_page = int(request.GET.get('page') or 1 )
    page = paginator.page(current_page)
    tasks_objects = page.object_list
    count = models.tasks.objects.count()
    contex = {'tasks_objects':tasks_objects ,
    'count':count,
    'paginator': paginator,
    'current_page' : current_page,
    'page':page,
    }
    return render(request,'list.html',contex)


def show_task(request,id):
    task = get_object_or_404(models.tasks , id = id)
    contex = {'task':task}
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
