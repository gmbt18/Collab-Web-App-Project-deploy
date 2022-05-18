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
    path('project/<int:id>/', views.projectPage, name='projectPage'),
    path('project/<int:id>/info', views.projectInfoPage, name='projectInfoPage'),
    path('project/<int:id>/members', views.projectMembersPage, name='projectMembersPage'),
    path('project/<int:id>/membersAdd', views.projectMembersAddPage, name='projectMembersAddPage'),
    path('project/<int:id>/history', views.projectHistoryPage, name='projectHistoryPage'),
    path('project/<int:id>/taskAdd', views.taskAddPage, name='taskAddPage'),
    path('project/<int:id>/task/<int:td>/taskEdit', views.taskEditPage, name='taskEditPage'),
    path('project/<int:id>/taskProgress', views.taskProgressPage, name='taskProgressPage'),
    path('leave/<int:id>/', views.leaveProject, name = 'leave'),
    path('delete/<int:id>/', views.deleteTask, name = 'deleteTask')
]
