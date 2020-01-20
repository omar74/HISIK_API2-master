from django.db import models
from user.models import User
from product.models import Product

class SearchQuerySet(models.QuerySet):
    pass

class SearchManager(models.Manager):
    def get_queryset(self):
        return SearchQuerySet(self.model,using=self._db)

class Search(models.Model):
    text            =  models.TextField(blank=False,null=False)
    user            =  models.ForeignKey(User,on_delete=models.CASCADE)
    product         =  models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)

    object = SearchManager()

    class Meta:
          verbose_name = "Search"
          verbose_name_plural = "User Search"

    def __str__(self):
        return '{0}'.format(self.text)