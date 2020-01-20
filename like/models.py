from django.db import models

from review.models import Review
from user.models import User

# Create your models here.
class Like(models.Model):
    review          =  models.ForeignKey(Review,on_delete=models.CASCADE)
    user            =  models.ForeignKey(User,on_delete=models.CASCADE)
    updated         =  models.DateTimeField(auto_now=True)
    timestamp       =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.user.username+" to " +self.review.id
        
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"