from django.db import models
from product.models import Product
from user.models import User
# Create your models here.
class Favourite(models.Model):
    product         =  models.ForeignKey(Product, on_delete=models.CASCADE)
    user            =  models.ForeignKey(User, on_delete=models.CASCADE)
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.user.UserName+" to " +self.product.name
        
    class Meta:
        verbose_name = "Favourite"
        verbose_name_plural = "Favourites"
