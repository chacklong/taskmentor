from django.db import models
from .task_flow import TaskFlow
# Create your models here.

# 学习节点
class LearningNode(models.Model):
    task_flow = models.ForeignKey(TaskFlow, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 外键关联到 TaskFlow
    task_flow = models.ForeignKey(TaskFlow, related_name='learning_node', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    progress = models.IntegerField(default=0)
    time_spent = models.DurationField(null=True, blank=True)