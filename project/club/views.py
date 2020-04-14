from django.shortcuts import render

# Create your views here.
def club(request):
  return render(request, 'club/club.html')

