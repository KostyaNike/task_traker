from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['discription', 'title', 'due_time', 'status', 'priority']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['due_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'all'),
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
        label='Select status:',
        widget=forms.Select(attrs={
            'class': 'choose',
            'style': 'visibility:hidden;'
        })
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']