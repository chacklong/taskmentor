# taskmanager/tests.py
from django.test import TestCase
from .models import user, task  # 这里导入你自定义的User模型

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = user.User.objects.create(username='testuser', email='test@test.com', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_task(self):
        task_lsit = task.Task.objects.create(name="Test Task", description="Test Description", user=self.user)
        self.assertEqual(task.Task.objects.count(), 1)
        self.assertEqual(task_lsit.name, "Test Task")
