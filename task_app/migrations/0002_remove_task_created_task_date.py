# Generated by Django 4.2.1 on 2023-06-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
