from django.contrib import admin
from django.db import models
# Register your models here.
class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=True)
    archive = models.BooleanField(default=True)