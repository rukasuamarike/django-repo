from django.db import models
from django.urls import reverse
# Create your models here.
class Ip(models.Model):
    time         = models.CharField(max_length=256)
    user   = models.TextField(blank=True, null=True)
    ip       = models.TextField(blank=True, null=True)

    def get_abs_url(self):
        return f"ipdyn/{self.id}/"
        #return reverse("ips",kwargs={"id":self.id})