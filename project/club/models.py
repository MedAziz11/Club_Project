from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Request (models.Model):
    status = (
        ('await', 'Await'),
        ('process', 'Accepted'),
        ('denied', 'Denied'),
    )
  
    statut = models.CharField(max_length=10, choices=status, default='await')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=50, blank=False, null=False)
    classe = models.CharField(max_length=5, blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False,default=timezone.now()  )
    description = models.TextField()
    note = models.TextField(blank=True, null=True)
    date_request =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.name.username } request"
