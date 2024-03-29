"""
URL configuration for tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseServerError

def redirect_to_home(request):
    return redirect("home")

def project_root_view(request):
    try:
        template = loader.get_template('accounts/landing_page.html')
        return HttpResponse(template.render())
    except Exception as e:
        # Log or print the exception for debugging purposes
        print(f"Error rendering template: {e}")
        # You can return a custom error page or redirect to another view
        return HttpResponseServerError("500 Internal Server Error")

urlpatterns = [
    # path("", redirect_to_home, name="home"),
    path("", project_root_view, name="project_root_view"),
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("accounts/", include("accounts.urls")),
    path("tasks/", include("tasks.urls")),
]



# def project_root_view(request):
#     return HttpResponse("This is the project root view.")
