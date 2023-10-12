from ..models.user import User
from ..models.task import Task
from ..models.reminder import Reminder
from ..models.permission import Permission
from ..serializers.task_serializer import TaskSerializer
from ..serializers.user_serializer import UserSerializer
from ..serializers.permission_serializer import PermissionSerializer
from ..serializers.reminder_serializer import ReminderSerializer
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class SmallPagination(PageNumberPagination):
    page_size = 20

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'task_type', 'difficulty']
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['created_at']
    pagination_class = SmallPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer