from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], default='medium')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tasks:task-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='comments_media/', blank=True, null=True)

class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('comment', 'user')