from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.reservacion)
"""
@admin.register(models.reservacion)
class reservacionAdmin(admin.ModelAdmin):
    pass
"""