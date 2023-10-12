from django.db import models
from .task_flow import TaskFlow
from .user import User
# Create your models here.

# 提醒表
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_flow = models.ForeignKey(TaskFlow, on_delete=models.CASCADE)
    reminder_type = models.CharField(max_length=50)
    reminder_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)