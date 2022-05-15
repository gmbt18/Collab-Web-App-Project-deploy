from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Collaborator(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    contact = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS = (
        ('To-Do', 'To-Do'),
        ('Doing', 'Doing'),
        ('Need Checking', 'Need Checking'),
        ('Done', 'Done')
    )
    
    name = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100,null=True,choices=STATUS)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name