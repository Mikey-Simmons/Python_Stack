from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.submit_book),
    path('authors',views.auths),
    path('addauth',views.submit_auth),
    path('books/<int:num>', views.book_page),
    path('add_auth_to_book',views.add_auth),
    path('authors/<int:num>',views.auth_page),
    path('add_book_to_auth',views.add_book)
]