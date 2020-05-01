
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from main.forms import RegisterForm
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def index_view(request):
  if request.user.is_authenticated: # we test if the user already authenticated
    if request.user.is_staff: # make redirection based on is_staff or not
      return HttpResponseRedirect(reverse('administration:admin_portal', args=()))
    elif not request.user.is_staff:
      return HttpResponseRedirect(reverse('club:club_portal', args=()))
  else: # if the user not authenticated, we must show him the login page
    return render(request, 'main/login.html')

def signup_view(request):
  if not request.user.is_authenticated:
    form = RegisterForm(request.POST or None)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      form.save()
      #subject = 'Welcome to ISIEVENT'
      #message = 'You created an account now '
      #recepient = str(form['email'].value())
      #send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False) for email verification
      user = User.objects.get(username=username)
      user.set_password(password)# because the form is making the password unusable for the authentification
      user.save()
      form = RegisterForm()
      return HttpResponseRedirect(reverse('main:index', args=()))
    return render(request, 'main/signup.html', {"form":form})
  return HttpResponseRedirect(reverse('main:index', args=()))


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
