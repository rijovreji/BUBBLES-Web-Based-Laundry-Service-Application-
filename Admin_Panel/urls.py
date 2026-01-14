from django.urls import path
from Admin_Panel import views

urlpatterns = [
    path('Base_admin/', views.Base_admin, name='Base_admin'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('Add_Service_admin/', views.Add_Service_admin, name='Add_Service_admin'),
    path('Save_service/', views.Save_service, name='Save_service'),
    path('View_Service_admin/', views.View_Service_admin, name='View_Service_admin'),
    path('Edite_serviese/<int:s_id>/', views.Edite_serviese, name='Edite_serviese'),
    path('update_servies/<int:s_id>/', views.update_servies, name='update_servies'),
    path('delete_Service/<int:s_id>/', views.delete_Service, name='delete_Service'),

]
