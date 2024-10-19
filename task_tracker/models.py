from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('done', 'Done')
    ]
    discription = models.TextField()
    title = models.CharField(max_length=250)
    due_time = models.DateTimeField(verbose_name='due_time', null=True, blank=True)
    status = models.CharField(max_length=27, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], default='medium')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')

    def __str__(self):
        return self.title
