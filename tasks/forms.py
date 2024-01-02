from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    start_date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT'],  
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
    )
    due_date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT'],  
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        )
