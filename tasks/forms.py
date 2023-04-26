from django import forms
from tasks.models import Task


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
