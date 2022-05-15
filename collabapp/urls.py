from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('dashboard', views.dashboardPage, name='dashboardPage'),
    path('login', views.loginPage, name='loginPage'),
    path('register', views.registerPage, name='registerPage'),
    path('account', views.accountPage, name='accountPage'),
    path('project', views.projectPage, name='projectPage'),
    path('projectInfo', views.projectInfoPage, name='projectInfoPage'),
    path('projectMembers', views.projectMembersPage, name='projectMembersPage'),
    path('projectHistory', views.projectHistoryPage, name='projectHistoryPage'),
    path('task', views.taskPage, name='taskPage'),
    path('taskProgress', views.taskProgressPage, name='taskProgressPage'),
]
