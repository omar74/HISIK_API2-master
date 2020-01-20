from django.contrib import admin
from .models  import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
     list_dispaly=('text','user')
     fields=[
             'text'
             ,'user'
        ]