from django.urls import path
from User_Web import views

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('', views.signin_signup, name='signin_signup'),
    path('saveUser_Registration/', views.saveUser_Registration, name='saveUser_Registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),

]
