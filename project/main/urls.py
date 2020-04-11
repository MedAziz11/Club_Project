from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index'), # route for the authentication page
    path('signup/', views.signup_view, name='signup'),#route for sign up page
    path('signup/register', views.register_view, name='register'),#register in the database
    #path('admin/', views.admin, name='admin_portal'), # route for the admin space
    path('login/', views.login_view, name='login'), # route for login
    path('logout/', views.logout_view, name='logout'), # route for logout
]