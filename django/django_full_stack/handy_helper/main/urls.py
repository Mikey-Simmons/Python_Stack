from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('welcome',views.welcome),
    path('logout',views.logout),
    path('login',views.login),
    path('new',views.newjob),
    path('addjob',views.addjob),
    path('jobs/<int:num>',views.displayjob),
    path('addjobtouser',views.addjob_to_user),
    path('jobs/edit/<int:num>',views.job_edit_page),
    path('editjob/<int:num>',views.editjob),
    path('delete',views.delete_job)
]