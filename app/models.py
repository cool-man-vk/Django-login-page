from django.db import models 
from django.utils import timezone
# Create your models here.
class Details(models.Model):
    item = models.CharField(max_length=200) 
    start_date = models.DateField() 
    end_date = models.DateField() 
    start_time = models.TimeField(default=timezone.now()) 
    end_time = models.TimeField(default=timezone.now())