from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homelogin, name='homelogin'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('homelogin/',views.homelogin, name='homelogin'),
   #path('register2/',views.register2, name='register2'),
   # path('login2/', views.user_login2, name='login2'),
   #path('logout/', views.user_logout2, name='logout2'),
#    path('homelogin/', views.home,name='homelogin'),
]