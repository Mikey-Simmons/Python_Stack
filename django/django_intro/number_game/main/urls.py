from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('number_guess', views.guess),
    path('correct', views.correct_answer),
    path('wrong',views.wrong_answer),
    path('wrong2',views.wrong2),

]