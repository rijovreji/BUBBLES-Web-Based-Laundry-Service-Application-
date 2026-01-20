from django.urls import path
from User_Web import views

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('', views.signin_signup, name='signin_signup'),
    path('saveUser_Registration/', views.saveUser_Registration, name='saveUser_Registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('Save_Contact/', views.Save_Contact, name='Save_Contact'),
    path('service_user/', views.service_user, name='service_user'),
    path('book_order/', views.book_order, name='book_order'),
    path('save_order/', views.save_order, name='save_order'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('service_detail/<int:s_id>/', views.service_detail, name='service_detail')

]
