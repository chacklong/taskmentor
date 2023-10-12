# /taskmanager/urls.py

from django.urls import path, include
from .views import api_views, general_views, task_flow_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'tasks', api_views.TaskViewSet)
router.register(r'permissions', api_views.PermissionViewSet)
router.register(r'reminders', api_views.ReminderViewSet)
router.register(r'task-flows', task_flow_views.TaskFlowViewSet )

urlpatterns = [
    path('', general_views.home, name='home'),
    path('api/',include(router.urls)),
    path('hello/',general_views.hello_world, name='hello_world'),
    path('tasks-list/', general_views.task_list, name='task_list'),
    # path('tasks/create/', views.create_task, name='create_task')
]