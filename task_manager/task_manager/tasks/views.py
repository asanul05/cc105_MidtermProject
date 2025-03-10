from django.shortcuts import render, redirect
from . models import Task

# Create your views here.

def task_list(request):
    task = Task.objects.all()
    return render(request, 'task_list.html', {'task': task})

# def task_form(request):
#     task = Task.objects.all()
#     return render(request, 'task_form.html', {'task': task})

def task_create(request):
    task = Task.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        newTask = Task (title=title, description= description, due_date =due_date)
        newTask.save()
        return redirect('/')
    return render(request, 'task_form.html', {'is_edit': False})


def task_update(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.save()
        return redirect('/')
    return render(request, 'task_form.html', {'task':task, 'is_edit': True})


def task_delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'task_confirm_delete.html', {'task':task})
    