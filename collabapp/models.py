from time import timezone
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Project(models.Model):
    code = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    contact = models.IntegerField(null=True)
    projects = models.ManyToManyField(Project, related_name= "members", blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS = (
        ('To-Do', 'To-Do'),
        ('Doing', 'Doing'),
        ('Need Checking', 'Need Checking'),
        ('Done', 'Done')
    )
    name = models.CharField(max_length=100, null=True)
    due_date = models.DateField()
    #project = models.ForeignKey(Project, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

