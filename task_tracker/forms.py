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
        label='',
        widget=forms.Select(attrs={
            'class': 'selectpicker',  # Устанавливаем класс для Bootstrap Select
            'style': 'display:none;'  # Скрываем оригинальный элемент select
        })
    )

    name = forms.CharField(
        max_length=100,
        required=True,
        label='Name',
        error_messages={'required': 'Заполните это поле.'}  # Кастомное сообщение об ошибке
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'media']
        widgets = {
            'media': forms.FileInput()
        }