from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)
