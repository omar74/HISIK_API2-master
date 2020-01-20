from django.contrib import admin
from .models import Review

@admin.register(Review)

class review_admin(admin.ModelAdmin):
    list_display=('id','user','text','rate','product')
    fields=[
            'text' ,
            'rate',
            'product',
            'user',
        ]
    