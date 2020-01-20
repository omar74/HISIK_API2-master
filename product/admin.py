from django.contrib import admin
from .models  import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_dispaly=('name','Description')
     fields=[
             'name'
             ,'Description'
             ,'ImageURL'
             ,'brand'
             ,'Category'
        ] 
