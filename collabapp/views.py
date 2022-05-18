import code
from distutils import log
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


    ##Prototype Dynamic User Display##
from .models import Profile,Project,Task
    ##Prototype Dynamic User Display##


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


        if Project.objects.filter(code=code).exists():
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
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
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
    puser = request.user.profile
    project = Project.objects.get(id=id)

    tasks_to_do = Task.objects.filter(project__id=project.id).filter(status="To-Do")
    ttd = list(tasks_to_do)

    tasks_doing = Task.objects.filter(project__id=project.id).filter(status="Doing")
    td = list(tasks_doing)

    tasks_needs_checking = Task.objects.filter(project__id=project.id).filter(status="Need Checking")
    tnc = list(tasks_needs_checking)

    tasks_done = Task.objects.filter(project__id=project.id).filter(status="Done")
    tdn = list(tasks_done)

    context = {'project':project, 'tasks_to_do': ttd, 'tasks_doing': td, "tasks_needs_checking": tnc, "tasks_done": tdn, 'user': puser}
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
    form = EditProjectForm(instance=project)

    if request.method == 'POST':
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            return redirect("projectPage", id=project.id)

    context = {'project':project, 'form': form}
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
def taskAddPage(request, id):
    task_form = TaskForm()
    project = Project.objects.get(id=id)
    
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            instance = task_form.save()
            instance.project = project
            instance.save()
            
            return redirect("projectPage", id=project.id)
    
    context = {'form': task_form, 'project': project}
    return render(request, 'collabapp/task-add.html', context)

@login_required(login_url='loginPage')
def taskEditPage(request, id, td):
    project = Project.objects.get(id=id)
    task = Task.objects.get(id=td)
    form = EditTaskForm(instance=task)

    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect("projectPage", id=project.id)

    context = {'project':project, 'task': task, 'form': form}
    return render(request, 'collabapp/task-edit.html', context)
    
@login_required(login_url='loginPage')    
def taskProgressPage(request):
    return render(request, 'collabapp/task-progress.html')
  
@login_required(login_url='loginPage')    
def navPage(request):
    p = request.user.profile.projects.all()
    pl = list(p)

    context = {'project': pl}
    return render(request, 'collabapp/navbar.html', context)

@login_required(login_url='loginPage')    
def leaveProject(request, id):
    user = request.user.profile
    proj = Project.objects.get(id=id)
    user.projects.remove(proj)
    return redirect("dashboardPage")

@login_required(login_url='loginPage')
def deleteTask(request, id):
    task = Task.objects.get(id=id)
    project = task.project.id
    task.delete()
    return redirect("projectPage", id=project)

@login_required(login_url='loginPage')
def joinTask(request, id):
    task = Task.objects.get(id=id)
    puser = request.user.profile
    puser.tasks.add(task)
    project = task.project.id
    return redirect("projectPage", id=project)
    
@login_required(login_url='loginPage')
def leaveTask(request, id):
    task = Task.objects.get(id=id)
    project = task.project.id
    puser = request.user.profile
    puser.tasks.remove(task)
    return redirect("projectPage", id=project)


def errorPageNotFound(request, exception):
    return render(request,'collabapp/page-not-found.html')


##Prototype Dynamic User Display##
def list_view(request):
    context ={}

    context ["dataset"] = Profile.objects.all()
        
    return render(request, "project-members.html", context)
##Prototype Dynamic User Display##