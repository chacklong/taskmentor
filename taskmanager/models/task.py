from django.db import models
from .user import User

# Create your models here.
# 任务表
class Task(models.Model):
    CYCLE_CHOICES = [
        ('Daily','每天'),
        ('Weekly','每周'),
    ]
    cylce = models.CharField(max_length=10, choices=CYCLE_CHOICES, default='Daily')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    task_type = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)