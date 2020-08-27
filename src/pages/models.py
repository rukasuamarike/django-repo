from django.db import models

# Create your models here.
class Log(models.Model):
    time         = models.CharField(max_length=256)
    user   = models.TextField(blank=True, null=True)
    ip       = models.TextField(blank=True, null=True)
