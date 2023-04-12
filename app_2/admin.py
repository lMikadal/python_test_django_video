from django.contrib import admin
from app_2.models import tPosition

# Register your models here.

class TAdmin(admin.ModelAdmin):
    list_display = ['id', 'position', 'status']

admin.site.register(tPosition, TAdmin)