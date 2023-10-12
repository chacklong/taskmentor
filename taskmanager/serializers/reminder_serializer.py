# taskmanager/serializers.py
from rest_framework import serializers
from ..models.reminder import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'