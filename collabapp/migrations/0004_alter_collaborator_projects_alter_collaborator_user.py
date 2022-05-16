# Generated by Django 4.0.4 on 2022-05-15 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collabapp', '0003_alter_collaborator_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='members', to='collabapp.project'),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]