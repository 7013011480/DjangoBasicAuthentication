from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
   # path('register/',Register.as_view()),
   path('login/', UserLogin.as_view()),
   path('getInfo/',GetUserInfo.as_view()),
   path('',views.index,name='index'),
   path('register/',views.register, name='register'),
]