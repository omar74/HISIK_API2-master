from django.db import models
from brand.models import Brand
from category.models import Category

class Product(models.Model):
    Description     =  models.TextField(blank=False,null=False)
    name            =  models.CharField(max_length=50,blank=False,null=False)
    ImageURL        =  models.URLField(blank=True,null=True)
    brand           =  models.ForeignKey(Brand,on_delete=models.CASCADE)
    Category        =  models.ForeignKey(Category,on_delete=models.CASCADE)
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return '{0}'.format(self.name)