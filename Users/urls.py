from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('hello/', views.Hello, name='hello'),
    path('users/', views.Users_list, name='users_list'),
    path('new_user/', views.Add_user, name='add_user'),
    path('user/', views.User_details, name='user_details'),
]
