from django.contrib import admin
from .models  import Scan
# Register your models here.

@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_dispaly=('user','product')
    fields=[
             'user'
             ,'product'
             ,'brand'
             ,'Category'
             ,'Blocked'
             ,'satisfy'
             ,'ImageURL'
        ]
