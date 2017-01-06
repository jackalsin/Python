from django.contrib import admin

# Register your models here.
from games import models

admin.site.register(models.Record)
