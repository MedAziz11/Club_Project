from django.urls import path
from . import views


app_name = 'club'
urlpatterns = [
    path('', views.club, name='club_portal'),  # route for the club space
    path('form/', views.submit_event_view, name='submit_event'), # the submittion of the event request and route to form page
    path('form/<pk>', views.form_view, name='view')
]