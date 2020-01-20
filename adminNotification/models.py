from django.db import models

from review.models import Review
from scan.models import Scan

# Create your models here.
class NotificationAdmin(models.Model):
      Status = models.NullBooleanField()
      Type = models.IntegerField(blank=False,null=False) 
      ProductReviewID = models.ForeignKey(Review,on_delete=models.CASCADE,null=True)
      ScanId = models.ForeignKey(Scan,on_delete=models.CASCADE,null=True)
      updated = models.DateTimeField(auto_now=True)
      timestamp = models.DateTimeField(auto_now_add=True)

      def __str__(self):
         return self.id
        
      class Meta:
         verbose_name = "Admin notifcaton "
         verbose_name_plural = "Admin notifcatons"