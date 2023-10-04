from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homelogin, name='homelogin'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('homelogin/',views.homelogin, name='homelogin'),
    path('userloginhome/',views.userloginhome, name='userloginhome'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_dashboard/users.html', views.users, name='users'),  # Define the URL pattern for users.html
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/login/',views.user_login,name='login'),
]
   #path('user_accounts/', views.user_accounts,name='user_accounts'),
    #path('forgotpassword/',views.forgotpassword, name='forgotpassword'),
    
    #path('register2/',views.register2, name='register2'),
    #path('login2/', views.user_login2, name='login2'),
   #path('logout/', views.user_logout2, name='logout2'),
    #path('homelogin/', views.home,name='homelogin'),

    