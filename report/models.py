from django.db import models
from django.db import models
from user.models import User
from product.models import Product

class ReportQuerySet(models.QuerySet):
    pass

class ReportManager(models.Manager):
    def get_queryset(self):
        return ReportQuerySet(self.model,using=self._db)

class Report(models.Model):
    product         =  models.ForeignKey(Product, on_delete=models.CASCADE)
    user            =  models.ForeignKey(User, on_delete=models.CASCADE)
    Description     =  models.TextField(blank=False,null=False)
    name            =  models.CharField(max_length=50,blank=False,null=False)
    brand           =  models.CharField(max_length=50,blank=False,null=False)
    category        =  models.CharField(max_length=50,blank=False,null=False)
    comment         =  models.TextField(blank=True,null=True)
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)

    object = ReportManager()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"