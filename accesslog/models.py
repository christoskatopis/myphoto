from django.conf import settings
from django.db import models
from django.utils import timezone


class AccessAttempt(models.Model):
 user_ip=models.CharField(max_length=100)
 user=models.CharField(max_length=150)
 login_attempts=models.PositiveIntegerField(default=1)
 attempt_time= models.DateTimeField(default=timezone.now)
 blocked=models.BooleanField(default=False)


 class Meta:
     ordering=['-attempt_time']

 def __unicode__(self):
        return self.user_ip+" attempt"
 