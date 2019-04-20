from django.db import models


# Create your models here.
class Donate(models.Model):

    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    amount=models.CharField(max_length=256)
    date_added=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='donate'
        ordering=['date_added']
    def __str__(self):
        return self.name
