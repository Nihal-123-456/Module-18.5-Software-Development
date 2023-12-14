from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('signup/',user_signup,name='signup'),
    path('login/',user_login,name='user_login'),
    path('profile/',user_profile,name='user_profile'),
    path('logout/',user_logout,name='user_logout'),
    path('change_password/',change_password,name='change_password'),
    path('change_password2/',change_password2,name='change_password2'),
]