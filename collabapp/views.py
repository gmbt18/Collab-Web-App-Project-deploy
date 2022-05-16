from distutils import log
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from .models import *
from .forms import *
# Create your views here.
# def index(request):
#     return render(request, 'catalog/dashboard.html')

def indexPage(request):
    # if not logged in
    # return render(request, 'collabapp/login.hmtl')

    # if logged in:
    return redirect('dashboardPage')

@login_required(login_url='loginPage')
def dashboardPage(request):
    return render(request, 'collabapp/dashboard.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboardPage')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboardPage')

		context = {}
		return render(request, 'collabapp/login.html', context)
def logOutPage(request):
    logout(request)
    return redirect('loginPage')

def registerPage(request):

    
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            Profile.objects.create(
                user=user,
                name=user.username,
                )

            messages.success(request, 'Account was created for ' + username)

            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'collabapp/register.html', context)

@login_required(login_url='loginPage')
def accountPage(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    else:
        form=EditProfileForm(instance=profile)
                
    context = {'profile': form}
    return render(request, 'collabapp/account.html', context)

@login_required(login_url='loginPage')
def projectPage(request):
    return render(request, 'collabapp/project-home.html')

@login_required(login_url='loginPage')
def projectNewPage(request):
    return render(request, 'collabapp/project-new.html')

@login_required(login_url='loginPage')
def projectInfoPage(request):
    return render(request, 'collabapp/project-info.html')

@login_required(login_url='loginPage')
def projectMembersPage(request):
    return render(request, 'collabapp/project-members.html')

@login_required(login_url='loginPage')
def projectMembersAddPage(request):
    return render(request, 'collabapp/project-members-add.html')

@login_required(login_url='loginPage')
def projectHistoryPage(request):
    return render(request, 'collabapp/project-history.html')

@login_required(login_url='loginPage')
def taskAddPage(request):
    return render(request, 'collabapp/task-add.html')

@login_required(login_url='loginPage')
def taskEditPage(request):
    return render(request, 'collabapp/task-edit.html')
    
@login_required(login_url='loginPage')    
def taskProgressPage(request):
    return render(request, 'collabapp/task-progress.html')
