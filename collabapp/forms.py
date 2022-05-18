from django import forms
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'code']

        labels = {
            'title' : 'Project Name',
            'code': 'Project Code'
        }

class TaskForm(ModelForm):
    status = forms.ChoiceField(choices=Task.STATUS)

    class Meta:
        model = Task
        fields = ['name', 'due_date', 'status']

        labels = {
            'name' : 'Task Name',
            'due_date' : 'Due Date',
            'status': 'Status'
        }

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','password']
        labels = {
            'email' : 'Email Address'
        }

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','contact','projects']

        labels = {
            'contact' : 'Contact No.',
        }

class EditProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'code', 'description']

        labels = {
            'title': 'Project Name',
            'code': 'Project Code',
            'description': 'Project Description'
        }

class EditTaskForm(ModelForm):
    status = forms.ChoiceField(choices=Task.STATUS)

    class Meta:
        model = Task
        fields = ['name', 'due_date', 'status']

        labels = {
            'name' : 'Task Name',
            'due_date' : 'Due Date',
            'status' : 'Status'
        }
