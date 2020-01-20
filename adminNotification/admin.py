from django.contrib import admin

from .models import NotificationAdmin

@admin.register(NotificationAdmin)
class Admin_AdminNotification(admin.ModelAdmin):
    list_display =  ('Status','Type','ProductReviewID','ScanId','timestamp')
    fields  = ('Status','Type','ProductReviewID','ScanId')
