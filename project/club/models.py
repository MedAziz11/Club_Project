from django.db import models
from django.utils import timezone

# Create your models here.
class Request (models.Model):
    status = (
        ('await', 'Await'),
        ('process', 'Accepted'),
        ('denied', 'Denied'),
    )
  
    statut = models.CharField(max_length=10, choices=status, default='await')
    name = models.CharField(max_length=30, blank=False, null=False)
    event = models.CharField(max_length=50, blank=False, null=False)
    classe = models.CharField(max_length=5, blank=False, null=False)
    date = models.DateTimeField(blank=True, null=True , default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.name
