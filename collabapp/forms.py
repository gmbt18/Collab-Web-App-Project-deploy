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
        fields = ['title']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'due_date']

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','password']

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','contact','projects']
