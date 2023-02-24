from django.db import models


# Create your models here.
class UseInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    phone = models.IntegerField()
    