from django.urls import path
from . import views



app_name = 'administration'
urlpatterns = [
    path('', views.admin, name='admin_portal'), 
    path('request/<pk>/', views.request_view, name='request_form'),
    path('request/<pk>/submit/', views.submit_view, name='submit_form'),
]