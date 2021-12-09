from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
   # path('register/',Register.as_view()),
   # path('login/', UserLogin.as_view()),
   path('getInfo/',GetUserInfo.as_view()),
   path('administrator/', views.administrator,name='administrator'),
   path('authenticUser/', views.authenticUser, name='authenticUser'),
   path('',views.index,name='index'),
   path('register/',views.register, name='register'),
   path('logout/',views.logout, name='logout'),
   path('login/', views.login, name='login'),
   path('loginPage/', views.loginPage, name='loginPage'),
]