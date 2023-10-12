# taskmanager/views/task_flow.py

from rest_framework import viewsets, permissions
from ..models.task_flow import TaskFlow
from ..serializers.task_flow_serializer import TaskFlowSerializer

# TaskFlowViewSet 用于处理与 TaskFlow 相关的请求
class TaskFlowViewSet(viewsets.ModelViewSet):
    # 查询集设置
    queryset = TaskFlow.objects.all()
    
    # 使用的序列化器
    serializer_class = TaskFlowSerializer

    # 仅允许认证的用户访问
    permission_classes = [permissions.IsAuthenticated]
    
    # ... 其他配置和方法
