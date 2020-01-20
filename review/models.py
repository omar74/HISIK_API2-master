from django.db import models

from user.models import User 
from product.models import Product 
# Create your models here.
class Review(models.Model):
    text            =  models.TextField(blank=False,null=False)
    rate            =  models.IntegerField(blank=True,null=True)
    product         =  models.ForeignKey(Product,on_delete=models.CASCADE)
    user            =  models.ForeignKey(User,on_delete=models.CASCADE)
    
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return '{0}'.format(self.text)