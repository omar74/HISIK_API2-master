from django.contrib import admin
from .models import NotificationUser

@admin.register(NotificationUser)
class Admin_NotificationUser(admin.ModelAdmin):
    list_display = ('Status','Type','notifyuser','owner','product','review')
    fields = ('Status','Type','notifyuser','owner','product','review')

