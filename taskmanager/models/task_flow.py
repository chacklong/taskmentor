from .task import Task
from django.db import models

# 任务流
class TaskFlow(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    progress_history = models.JSONField(default=list)

    # 状态选项
    status_choices = [
        ('NOT_STARTED', 'Not Started'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    # 状态字段
    status = models.CharField(
        max_length=12,
        choices=status_choices,
        default='NOT_STARTED',
    )