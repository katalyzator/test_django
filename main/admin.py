from django.contrib import admin

# Register your models here.
from main.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
