from django.contrib import admin
from .models import user, task , task_flow, learning_node, reminder, permission

# Register your models here.
admin.site.register(user.User)
admin.site.register(task.Task)
admin.site.register(task_flow.TaskFlow)
admin.site.register(learning_node.LearningNode)
admin.site.register(reminder.Reminder)
admin.site.register(permission.Permission)

