# Generated by Django 4.2.1 on 2023-06-11 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0003_remove_todo_close_date_todo_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='result',
            new_name='is_complete',
        ),
    ]
