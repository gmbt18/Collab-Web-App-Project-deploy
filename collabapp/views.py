from distutils import log
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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
    puser = request.user.profile

    if request.method == 'POST':
        code = request.POST.get('code')
        proj = Project.objects.get(code=code)
        puser.projects.add(proj)

        return redirect("dashboardPage")

    else:
        p = request.user.profile.projects.all()
        pl = list(p)

    context = {'projects': pl}
    return render(request, 'collabapp/dashboard.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboardPage')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

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
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user.profile)
        u = EditUserForm(request.POST, instance=request.user)
        pw = PasswordChangeForm(data=request.POST, user=request.user )
        if form.is_valid() and u.is_valid():
            form.save()
            u.save()
            
        if pw.is_valid():
            pw.save()
            update_session_auth_hash(request, pw.user)
           
        return redirect('accountPage')

    else:
        form=EditProfileForm(instance=request.user.profile)
        u = EditUserForm(instance=request.user)
        pw = PasswordChangeForm(request.user)
        context = {'profile': form,'usr': u, 'pw':pw}
        return render(request, 'collabapp/account.html', context) 

       
    

@login_required(login_url='loginPage')
def projectPage(request, id):
    project = Project.objects.get(id=id)
    context = {'project':project}
    return render(request, 'collabapp/project-home.html', context)

@login_required(login_url='loginPage')
def projectNewPage(request):
    project_form = ProjectForm()
    user = request.user.profile
    
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            instance=project_form.save(commit=False)
            instance.owner=request.user
            instance.save()
            proj = Project.objects.get(code=instance.code)
            user.projects.add(proj)
            

            return redirect("dashboardPage")

    context = {'form': project_form}
    return render(request, 'collabapp/project-new.html', context)

@login_required(login_url='loginPage')
def projectInfoPage(request, id):
    project = Project.objects.get(id=id)
    context = {'project':project}
    return render(request, 'collabapp/project-info.html', context)

@login_required(login_url='loginPage')
def projectMembersPage(request, id):
    project = Project.objects.get(id=id)
    context = {'project':project}
    return render(request, 'collabapp/project-members.html', context)

@login_required(login_url='loginPage')
def projectMembersAddPage(request, id):
    project = Project.objects.get(id=id)
    context = {'project':project}
    return render(request, 'collabapp/project-members-add.html', context)

@login_required(login_url='loginPage')
def projectHistoryPage(request, id):
    project = Project.objects.get(id=id)
    context = {'project':project}
    return render(request, 'collabapp/project-history.html', context)

@login_required(login_url='loginPage')
def taskAddPage(request):
    task_form = TaskForm()
    
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("projectPage")
    
    context = {'form': task_form}
    return render(request, 'collabapp/task-add.html', context)

@login_required(login_url='loginPage')
def taskEditPage(request):
    return render(request, 'collabapp/task-edit.html')
    
@login_required(login_url='loginPage')    
def taskProgressPage(request):
    return render(request, 'collabapp/task-progress.html')

@login_required(login_url='loginPage')    
def navPage(request):
    p = request.user.profile.projects.all()
    pl = list(p)

    context = {'project': pl}
    return render(request, 'collabapp/navbar.html', context)