from django.db import models

# Create your models here.
class details(models.Model):
    donors=models.CharField(max_length=256)
    raised=models.CharField(max_length=256)
    exp=models.CharField(max_length=256)
    countries=models.CharField(max_length=256)
