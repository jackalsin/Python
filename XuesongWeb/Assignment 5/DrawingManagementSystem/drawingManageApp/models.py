from django.db import models

# Create your models here.
class Drawing(models.Model):
    DrawingID = models.CharField(max_length=10)
    BuildingName = models.CharField(max_length=20)
    ConstructedYear = models.IntegerField()
    Contractor = models.CharField(max_length=20)
    Floor = models.CharField(max_length=4)
    Shop = models.CharField(max_length=10)