from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Memo(models.Model):
    Name = models.CharField(max_length=10)
    Text = models.CharField(max_length=140)
    Email = models.CharField(max_length=140)
    Phone = models.CharField(max_length=20)
