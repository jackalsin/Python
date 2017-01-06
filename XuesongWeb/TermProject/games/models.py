from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Record(models.Model):
    username = models.CharField(max_length=20)
    score = models.IntegerField()
