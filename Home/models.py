from django.db import models

# Create your models here.
class Count(models.Model):
    name = models.CharField(max_length=100)
    visitors = models.IntegerField(default=0)