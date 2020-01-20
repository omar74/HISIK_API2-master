from django.db import models

from myadmin.models import Admin


class User(models.Model):
    FirstName       =  models.CharField(max_length=50,blank=False,null=False,default="")
    LastName        =  models.CharField(max_length=50,blank=False,null=False,default="")
    UserName        =  models.CharField(max_length=50,unique=True,blank=False,null=False,default="")
    Password        =  models.CharField(max_length=50,blank=False,null=False,default="")
    Email           =  models.EmailField(blank=False,null=False,default="",unique=True)
    DeviceID        =  models.CharField(max_length=100,blank=False,null=False,default="")
    FCMToken        =  models.CharField(max_length=200,blank=False,null=False,default="")
    #IP              =  models.GenericIPAddressField(blank=False,null=False,unique=True,protocol='both',unpack_ipv4=False)
    Status          =  models.NullBooleanField()
    ImageURL        =  models.URLField(blank=True,null=True)
    WarningScore    =  models.IntegerField(blank=True,null=True)
    BlockedBy       =  models.ForeignKey(Admin,on_delete=models.CASCADE,blank=True,default="",null=True)
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
 
    def __str__(self):
        return '{0}'.format(self.UserName)

