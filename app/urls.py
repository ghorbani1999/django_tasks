from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks , name='list' ),
    path('<int:id>', views.show_task , name= 'show_task'),
    path('<int:id>/edit' , views.edit_task , name='edit_task'),
    path('<int:id>/delete' , views.delete_task , name='delete_task'),
    path('create' , views.create_task , name= 'create_task'),
]