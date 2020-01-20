from django.contrib import admin
from .models import Replay

@admin.register(Replay)

class replay_admin(admin.ModelAdmin):
    list_display=('id','review','user','text')
    fields=[
            
            'review',
            'user',
            'text' ,
        ]
    