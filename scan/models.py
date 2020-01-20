from django.db import models
from brand.models import Brand
from category.models import Category
from user.models import User
from product.models import Product

class Scan(models.Model):
    ImageURL        =  models.URLField(blank=True,null=True)
    Blocked         =  models.NullBooleanField()
    brand           =  models.ForeignKey(Brand,on_delete=models.CASCADE,default="",blank=True,null=True)
    Category        =  models.ForeignKey(Category,on_delete=models.CASCADE,default="",blank=True,null=True)
    user            =  models.ForeignKey(User,on_delete=models.CASCADE)
    product         =  models.ForeignKey(Product,on_delete=models.CASCADE,default="",blank=True,null=True)
    satisfy         =  models.NullBooleanField()
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Scan"
        verbose_name_plural = "User Scanns"

    def __str__(self):
         return '{0}'.format(self.user.UserName)