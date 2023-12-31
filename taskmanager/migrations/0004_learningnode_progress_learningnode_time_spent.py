# Generated by Django 4.2.3 on 2023-10-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "taskmanager",
            "0003_alter_learningnode_name_alter_learningnode_task_flow_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="learningnode",
            name="progress",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="learningnode",
            name="time_spent",
            field=models.DurationField(blank=True, null=True),
        ),
    ]
