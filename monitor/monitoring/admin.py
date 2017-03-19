from django.contrib import admin
from .models import LogEntry

# Register your models here.

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # list_display = ('ip_address')
    pass