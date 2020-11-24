from django.urls import path     
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new',views.new_show_page),
    path('addshow',views.add_show),
    path('shows/<int:num>',views.show_display),
    path('shows/<int:num>/edit',views.edit_show_page),
    path('editshow',views.edit_show)
]