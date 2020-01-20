from django.db import models
from user.models import User
from review.models import Review 
from product.models import Product
# Create your models here.
class NotificationUser(models.Model):
    Status     = models.NullBooleanField()
    Type       = models.IntegerField() 
    notifyuser = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_notifyuser',default="")
    owner      = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    product    = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    review     = models.ForeignKey(Review,on_delete=models.CASCADE,null=True)
    updated    = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User notification"
        verbose_name_plural = "Users notificaions"

    def __str__(self):
        return '{0}'.format(self.owner.UserName)