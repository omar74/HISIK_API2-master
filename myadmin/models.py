from django.db import models

# Create your models here.

class Admin(models.Model):
  Role = models.IntegerField(blank=False,null=False)
  Name = models.CharField(max_length=50,blank=False,null=False) 
  password=models.CharField(max_length=20,blank=False,null=False) 
  IP = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
  Email = models.EmailField(blank=False,null=False)
  Token = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return self.Name
        
  class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

