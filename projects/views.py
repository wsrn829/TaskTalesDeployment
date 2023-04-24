from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project


# Create your views here.
def list_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/list_projects.html", context)
