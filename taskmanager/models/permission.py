from django.db import models
from .user import User

# Create your models here.

# 权限模型
class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(User, related_name='permissions')

    def __str__(self):
        return self.name