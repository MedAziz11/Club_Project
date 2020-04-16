from django.shortcuts import render
from .models import Request
from django.contrib.auth.models import User
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def club(request):
  all_requests = Request.objects.all()
  today = datetime.now()
  todays_events = [request for request in all_requests if request.date.date() == today.date() and request.statut=='process']  
  clubs = User.objects.count()-1
  club_requests = Request.objects.filter(name=request.user).order_by('-date_request')
  accepted = Request.objects.filter(name=request.user, statut='process').count()
  denied = Request.objects.filter(name=request.user, statut='denied').count()
  awaits =  Request.objects.filter(name=request.user, statut='await')
  context ={
    'requests_list': club_requests ,
    'events_list': todays_events , 
    'today': today.strftime("%d %B , %Y"),
    'clubs': clubs ,
    'accepted': accepted,
    'denied' : denied,
    'awaits': awaits.count(), 
    'notification':'has-noti' if accepted>0 or denied>0  else '',
  }
  return render(request, 'club/club.html', context)

def form_view(request):
  return render(request, 'club/club_request.html')

def submit_event_view(request):
  if request.method=='POST':
    event = request.POST.get('event')
    classe = request.POST.get('classe')
    description = request.POST.get('description')
    request = Request(name=request.user, event=event, classe=classe, description=description)
    request.save()
    return  HttpResponseRedirect(reverse('club:club_portal',args=() ))
    


    
