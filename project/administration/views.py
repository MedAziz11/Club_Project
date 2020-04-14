from django.shortcuts import render,redirect
from club.models import Request
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.
def admin(request):
  all_requests = Request.objects.all()
  today = datetime.now()
  todays_events = [request for request in all_requests if request.date.date() ==today.date()]  
  clubs = User.objects.count()-1
  accepted = Request.objects.filter(statut='process').count()
  denied = Request.objects.filter(statut='denied').count()
  awaits =  Request.objects.filter(statut='await')
  context ={
    'requests_list': all_requests ,
    'events_list': todays_events , 
    'today': today.strftime("%d %B , %Y"),
    'clubs': clubs ,
    'accepted': accepted,
    'denied' : denied,
    'awaits_all'
    'awaits': awaits.count(), 
    'notification':'has-noti' if awaits.count()>0 else ''
  }
  return render(request, 'admin/admin.html', context)

def request_view(request , pk):
  club_request = Request.objects.get(pk=pk)
  context={
    'club':club_request.name,
    'event' :club_request.event,
    'classe' : club_request.classe,
    'date' : club_request.date,
    'description' : club_request.description,
  }
  return render(request, 'admin/request_form.html', context)
