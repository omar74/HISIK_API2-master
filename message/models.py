from django.db import models
from user.models import User

class MassageQuerySet(models.QuerySet):
    pass

class MassageManager(models.Manager):
    def get_queryset(self):
        return MassageQuerySet(self.model,using=self._db)

class Message(models.Model):
    text       = models.TextField(blank=True,null=True)
    user       = models.ForeignKey(User,on_delete=models.CASCADE)
    updated    = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    object = MassageManager()

    def __str__(self):
            return self.text
        
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"