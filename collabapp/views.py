from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request, 'catalog/dashboard.html')

def indexPage(request):
    # if not logged in
    # return render(request, 'collabapp/login.hmtl')

    # if logged in:
    return redirect('dashboardPage')

def dashboardPage(request):
    return render(request, 'collabapp/dashboard.html')

def loginPage(request):
    return render(request, 'collabapp/login.html')

def accountPage(request):
    return render(request, 'collabapp/account.html')

def projectPage(request):
    return render(request, 'collabapp/project-home.html')

def projectInfoPage(request):
    return render(request, 'collabapp/project-info.html')

def taskPage(request):
    return render(request, 'collabapp/edit-task.html')