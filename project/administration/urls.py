from django.urls import path
from . import views


app_name = 'administration'
urlpatterns = [
    path('', views.admin, name='admin_portal'),  # route for the club space
]