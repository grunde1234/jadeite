from django.db import models

# Create your models here.
class Courses(models.Model):
    coursename = models.CharField(max_length=30)
    coursecode = models.CharField(max_length=10, blank=True, null=True)
    level = models.CharField(max_length=3, blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    fee = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
   