from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from main.forms import ProfileForm
from .models import Request
from django.utils import timezone


# Create your views here.**


@login_required(login_url="main:index")
def club(request):
    all_requests = Request.objects.all()
    today = timezone.now()
    todays_events = [request for request in all_requests if request.date.date() == today.date() and request.statut=='process']  
    Request.objects.filter(date__lte=today).delete()# __lte less than and equall
    clubs = User.objects.count()-1
    club_requests = Request.objects.filter(name=request.user).order_by('-date_request')
    accepted = Request.objects.filter(name=request.user, statut='process').count()
    denied = Request.objects.filter(name=request.user, statut='denied').count()
    awaits =  Request.objects.filter(name=request.user, statut='await')
    form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    form.save()
    context ={
      'requests_list': club_requests ,
      'requests_not_await': club_requests.exclude(statut="await") ,
      'events_list': todays_events , 
      'today': today.strftime("%d %B , %Y"),
      'clubs': clubs ,
      'accepted': accepted,
      'denied' : denied,
      'awaits': awaits.count(), 
      'notification':'has-noti' if accepted>0 or denied>0  else '',
      'form':form,
    }
    return render(request, 'club/club.html', context)

@login_required(login_url="main:index")
def submit_event_view(request):
  if request.method=='POST':
    event = request.POST.get('event')
    classe = request.POST.get('classe')
    description = request.POST.get('description')
    date = request.POST.get('date')
    request = Request(name=request.user, event=event, classe=classe, description=description ,date=date)
    request.save()
    return  HttpResponseRedirect(reverse('club:club_portal',args=() ))
  return render(request, 'club/club_request.html',)
    


@login_required(login_url="main:index")
def form_view(request , pk):
  club_request = Request.objects.get(pk=pk)
  if club_request.name==request.user: 
    if not request.user.is_staff :
      accepted = Request.objects.filter(name=request.user, statut='process').count()
      denied = Request.objects.filter(name=request.user, statut='denied').count()#for the notifications
      club_requests = Request.objects.filter(name=request.user)#for notification
    
      context={
        'requests_not_await': club_requests.exclude(statut="await") ,
        'pk':club_request.pk,
        'club':club_request.name,
        'event' :club_request.event,
        'classe' : club_request.classe,
        'date' : club_request.date,
        'description' : club_request.description,
        'note': club_request.note if club_request.note != None else 'No Notes for you' ,
        'notification':'has-noti' if accepted>0 or denied>0  else '',
      }
      return render(request, 'club/view_form.html', context)
    else:
      return Http404()
  return  HttpResponseRedirect(reverse('club:club_portal',args=() ))
