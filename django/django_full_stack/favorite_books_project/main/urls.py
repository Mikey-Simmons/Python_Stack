from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('books',views.books),
    path('logout',views.logout),
    path('login',views.login),
    path('addbook',views.addbook),
    path('addfav',views.addfav),
    path('books/<int:num>',views.displaybook),
    path('removefav',views.removefav),
    path('editbook',views.editbook)
]