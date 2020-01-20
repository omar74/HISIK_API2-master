from django.db import models
from review.models import Review
from user.models import User
# Create your models here.
class Replay(models.Model):
    review          =  models.ForeignKey(Review,on_delete=models.CASCADE)
    user            =  models.ForeignKey(User,on_delete=models.CASCADE)
    text            =  models.TextField(blank=False,null=False)
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
        
    class Meta:
        verbose_name = "Replay"
        verbose_name_plural = "Replies"