# Generated by Django 5.1.3 on 2024-12-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_todo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]