from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('submitted_dojo', views.submit_dojo),
    path('submitted_ninja',views.submit_ninja)
]