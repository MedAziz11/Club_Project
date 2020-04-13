from django.shortcuts import render
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
  awaits =  Request.objects.filter(statut='await').count()
  context ={
    'requests_list': all_requests ,
    'events_list': todays_events , 
    'today': today.strftime("%d %B , %Y"),
    'clubs': clubs ,
    'accepted': accepted,
    'denied' : denied,
    'awaits': awaits, 
    'notification':'has-noti' if awaits>0 else ''
  }
  return render(request, 'admin/admin.html', context)

