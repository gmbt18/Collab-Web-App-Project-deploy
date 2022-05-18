from time import timezone
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    code = models.CharField(max_length=255, null=True, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
    @property
    def getmembertotal(self):
        m = self.members.all()
        mem = list(m)
        total = len(mem)
        s = str(total)
        if total > 1:
            return "Members: " + s
        else:
            return "Member: " + s

class Task(models.Model):
    STATUS = (
        ('To-Do', 'To-Do'),
        ('Doing', 'Doing'),
        ('Need Checking', 'Need Checking'),
        ('Done', 'Done')
    )
    name = models.CharField(max_length=100, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS, default = "To-Do")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", null=True)
    
    def __str__(self):
        return self.name

    @property
    def getMembers(self):
        task = self.task_members.all()
        t = list(task)
        return t


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to = '', default='/default_pfp.png')
    projects = models.ManyToManyField(Project, related_name= "members", blank=True)
    tasks = models.ManyToManyField(Task, related_name= "task_members", blank=True)


    def __str__(self):
        return self.name

