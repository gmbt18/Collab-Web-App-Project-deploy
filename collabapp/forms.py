from django import forms
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'due_date']

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email', 'contact']