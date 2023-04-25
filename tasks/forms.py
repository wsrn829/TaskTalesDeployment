from django import forms
from tasks.models import Task
from projects.models import Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        )
