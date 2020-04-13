
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


#def index_view(request):
#  return render(request, 'main/login.html')

def index_view(request):
  if request.user.is_authenticated: # we test if the user already authenticated
    if request.user.is_staff: # make redirection based on is_staff or not
      return HttpResponseRedirect(reverse('administration:admin_portal', args=()))
    elif not request.user.is_staff:
      return HttpResponseRedirect(reverse('club:club_portal', args=()))
  else: # if the user not authenticated, we must show him the login page
    return render(request, 'main/login.html')

def signup_view(request):
  return render(request, 'main/signup.html')

def register_view(request):
  name = request.POST.get('name')
  search = User.objects.filter(username=name)
  if request.method =="POST" and len(search)==0 :
    email = request.POST.get('email')
    password = request.POST.get('pass')
    user = User.objects.create_user(name, email, password)
    user.save()
    #return HttpResponseRedirect(reverse('main:index', args=()))
    return render(request, 'main/login.html',  {'created':'Account created succesfully'})
  else:
    return render(request, 'main/signup.html',  {'exist':'Club Alredy exists'})

def login_view(request):
  username = request.POST.get('name', False)
  password = request.POST.get('pass', False)
  user = authenticate(username=username, password=password)   #autheticate
  if user is not None and user.is_active: # if the authetication goes well and the user is active
    login(request, user) # do the login in django system
    if user.is_staff:
      return HttpResponseRedirect(reverse('administration:admin_portal', args=()))
    elif not user.is_staff:
      return HttpResponseRedirect(reverse('club:club_portal', args=()))
  else:
    return render(request, 'main/login.html', { 'notexist':'Club doesnt exist or false password ' })

def logout_view(request):
  logout(request)
  return render(request, 'main/login.html')


#def admin(request):
#  return render(request, 'main/admin.html')
