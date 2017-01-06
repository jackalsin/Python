from django.contrib import admin

# Register your models here.
from TodoListApp import models

admin.site.register(models.Task)
