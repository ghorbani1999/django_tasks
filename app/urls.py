from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.list_tasks , name='list' ),
    path('tasks/<int:id>', views.show_task , name= 'show_task'),
    path('tasks/<int:id>/edit' , views.edit_task , name='edit_task'),
    path('tasks/<int:id>/delete' , views.delete_task , name='delete_task'),
    path('tasks/create' , views.create_task , name= 'create_task'),

    # persons paths :

    path('persons/', views.list_persons , name='list_persons' ),
    path('persons/<int:id>/edit' , views.edit_person , name='edit_person'),
    path('persons/<int:id>/delete' , views.delete_person , name='delete_person'),
    path('persons/create' , views.create_person , name= 'create_person'),
]