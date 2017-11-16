from django.db import models
from django.conf import settings


class Order(models.Model):
 amount=models.PositiveIntegerField()
 date_created=models.DateTimeField(auto_now=False,auto_now_add=True)
 user= models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
 is_completed=models.BooleanField(default=False)


