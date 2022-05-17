from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('dashboard/', views.dashboardPage, name='dashboardPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout/', views.logOutPage, name="logout"),
    path('register', views.registerPage, name='registerPage'),
    path('account/', views.accountPage, name='accountPage'),
    path('project-new', views.projectNewPage, name='projectNewPage'),
    path('project', views.projectPage, name='projectPage'),
    path('projectInfo', views.projectInfoPage, name='projectInfoPage'),
    path('projectMembers', views.projectMembersPage, name='projectMembersPage'),
    path('projectMembersAdd', views.projectMembersAddPage, name='projectMembersAddPage'),
    path('projectHistory', views.projectHistoryPage, name='projectHistoryPage'),
    path('taskAdd', views.taskAddPage, name='taskAddPage'),
    path('taskEdit', views.taskEditPage, name='taskEditPage'),
    path('taskProgress', views.taskProgressPage, name='taskProgressPage'),
]
