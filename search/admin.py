from django.contrib import admin
from .models  import Search

@admin.register(Search)
class MessageAdmin(admin.ModelAdmin):
     list_dispaly=('text','user')
     fields=[
             'text'
             ,'user'
             ,'product'
        ]