from django.shortcuts import render,redirect
from club.models import Request
from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def admin(request):
  all_requests = Request.objects.all()
  today = datetime.now()
  todays_events = [request for request in all_requests if request.date.date() ==today.date()and request.statut=='process']  
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
    'awaits': awaits.count(), 
    'notification':'has-noti' if awaits.count()>0 else ''
  }
  return render(request, 'admin/admin.html', context)

def request_view(request , pk):
  if request.user.is_staff:
    awaits =  Request.objects.filter(statut='await')
    club_request = Request.objects.get(pk=pk)
    context={
      'pk':club_request.pk,
      'club':club_request.name,
      'event' :club_request.event,
      'classe' : club_request.classe,
      'date' : club_request.date,
      'description' : club_request.description,
      'statut' : club_request.statut if club_request.statut=='process' else None ,
      'notification':'has-noti' if awaits.count()>0 else ''
    }
    return render(request, 'admin/request_form.html', context)
  return  HttpResponseRedirect(reverse('administration:admin_portal',args=() ))

def submit_view(request, pk):
  if request.method =='POST':
    statut = request.POST.get('radios')
    note = request.POST.get('note')
    print(note)
    update = Request.objects.get(pk=pk)
    if statut==None :
      update.statut="await"
    else:
      update.statut=statut
    update.note=note
    update.save()
    return  HttpResponseRedirect(reverse('administration:admin_portal',args=() ))
