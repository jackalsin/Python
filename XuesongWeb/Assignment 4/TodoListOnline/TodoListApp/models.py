from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Task(models.Model):
    TaskId = models.CharField(max_length=8)
    Description = models.CharField(max_length=30)
    DueDate = models.DateField()
    # true means finished, false means unfinished.
    Status = models.BooleanField()
