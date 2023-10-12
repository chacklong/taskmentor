from rest_framework import serializers
from ..models.task_flow import TaskFlow

# TaskFlowSerializer 用于序列化 TaskFlow模型
class TaskFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFlow
        fields = '__all__'