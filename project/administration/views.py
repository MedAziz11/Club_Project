from django.shortcuts import render,redirect
from club.models import Request
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from main.forms import ProfileForm
from django.utils import timezone
# Create your views here.


@login_required
def admin(request):
  all_requests = Request.objects.all().order_by('-date_request')
  today = timezone.now()
  todays_events = [request for request in all_requests if request.date.date() ==today.date()and request.statut=='process']  
  clubs = User.objects.count()-1
  accepted = Request.objects.filter(statut='process').count()
  denied = Request.objects.filter(statut='denied').count()
  awaits =  Request.objects.filter(statut='await')
  form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
  form.save()
  context ={
    'requests_list': all_requests ,
    'events_list': todays_events , 
    'today': today.strftime("%d %B , %Y"),
    'clubs': clubs ,
    'accepted': accepted,
    'denied' : denied,
    'awaits': awaits.count(), 
    'notification':'has-noti' if awaits.count()>0 else '',
    'form' : form,
  }
  return render(request, 'admin/admin.html', context)


@login_required
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


@login_required
def submit_view(request, pk):
  if request.method =='POST':
    statut = request.POST.get('radios')
    note = request.POST.get('note')
    update = Request.objects.get(pk=pk)
    if statut==None :
      update.statut="await"
    else:
      update.statut=statut
    update.note=note
    update.save()
    return  HttpResponseRedirect(reverse('administration:admin_portal',args=() ))
