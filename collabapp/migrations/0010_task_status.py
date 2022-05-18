# Generated by Django 4.0.4 on 2022-05-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabapp', '0009_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('To-Do', 'To-Do'), ('Doing', 'Doing'), ('Need Checking', 'Need Checking'), ('Done', 'Done')], default='To-Do', max_length=100),
        ),
    ]
