from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('dashboard', views.dashboardPage, name='dashboardPage'),
    path('login', views.loginPage, name='loginPage'),
    path('account', views.accountPage, name='accountPage'),
    path('project', views.projectPage, name='projectPage'),
    path('projectInfo', views.projectInfoPage, name='projectInfoPage'),
    path('task', views.taskPage, name='taskPage'),
]