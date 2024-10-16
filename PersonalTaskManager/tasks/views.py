from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Tasks
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def task_list(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, "task_list.html", {"tasks": tasks})


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm()
    return render(request, "add_task.html", {"form": form})


@login_required
def update_task(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "update_task.html", {"form": form})


@login_required
def delete_task(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:task_list")
    return render(request, "delete_task.html", {"task": task})
