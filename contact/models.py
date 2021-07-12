from django.db import models

# Create your models here.
class Query(models.Model):
    Name = models.CharField(max_length=200, blank=False)
    Email = models.EmailField(blank=False)
    Desc = models.TextField(blank=False)
    
    def __str__(self):
        return str(self.Name) + " - " + str(self.Email)