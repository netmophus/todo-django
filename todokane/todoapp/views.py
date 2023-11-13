from django.shortcuts import render, redirect,get_object_or_404
from .models import Task



# Create your views here.
def todos(request):
  tasks = Task.objects.filter(is_completed=False).order_by('-update_at')
  completed_tasks = Task.objects.filter(is_completed=True)
  context = {
    'tasks': tasks,
    'completed_tasks': completed_tasks
  }
  return render(request, 'todo/index.html',context)

def addtask(request):
  task = request.POST['task']
  print(request.POST)
  Task.objects.create(task=task)
  return redirect('/')

def taskrealise(request, pk):
  task_realise = get_object_or_404(Task, pk=pk)
  task_realise.is_completed = True
  task_realise.save()
  return redirect('/')

def taskmodifie(request, pk):
  task_modifie = get_object_or_404(Task, pk=pk)
  task_modifie.is_completed = False
  task_modifie.save()
  return redirect('/')

def taskupdate(request, pk):
  get_task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST' :
    new_task = request.POST['name']
    get_task.task = new_task
    get_task.save()
    return redirect('/')
  else : 
    context = {
      'get_task': get_task
    }  
  return render(request, 'todo/edit_task.html', context)


def deletetask(request,pk):
  del_task = get_object_or_404(Task, pk=pk)
  del_task.delete()
  return redirect('/')


 
  