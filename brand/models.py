from django.db import models

# Create your models here.
class Brand(models.Model):
    Name       = models.CharField(max_length=50,blank=False,null=False,unique=True)
    updated    = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
        
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
