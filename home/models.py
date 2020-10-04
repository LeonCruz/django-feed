from django.db import models
from django.utils import timezone


# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    rss_site = models.CharField(max_length=300, unique=True)
    date_add = models.DateTimeField(auto_now=True)
