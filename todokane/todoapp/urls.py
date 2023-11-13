
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.todos, name='todos-index'),
    path('addtask/', views.addtask, name='add-task'),
    path('taskrealise/<int:pk>/', views.taskrealise, name='task-realise'),
    path('taskmodifie/<int:pk>/', views.taskmodifie, name='task-modifie'),
    path('edittask/<int:pk>/', views.taskupdate, name='edit-task'),
    path('deltask/<int:pk>/', views.deletetask, name='del-task'),
    
]
