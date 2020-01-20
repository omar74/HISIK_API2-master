from django.contrib import admin
from .models import Like

@admin.register(Like)

class replay_admin(admin.ModelAdmin):
    list_display=('review','user')
    fields=[
            'review',
            'user',
             
        ]
    