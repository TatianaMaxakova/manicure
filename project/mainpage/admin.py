from django.contrib import admin

from . import models
  
# Register your models here. 
 
@admin.register(models.Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in models.Person._meta.get_fields()]
