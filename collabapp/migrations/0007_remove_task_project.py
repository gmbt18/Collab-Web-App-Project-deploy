# Generated by Django 4.0.4 on 2022-05-16 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collabapp', '0006_rename_collaborator_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
    ]