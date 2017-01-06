from django.contrib import admin

# Register your models here.
from memo import models

admin.site.register(models.Memo)
