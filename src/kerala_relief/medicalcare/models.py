from django.db import models

# Create your models here.
class Hospital(models.Model):
    name=models.CharField(max_length=256)
    total_strength=models.PositiveIntegerField(null=True)
    availability=models.BooleanField(default=True)
    location=models.TextField(blank=True)
    latitude=models.CharField(max_length=256)
    longitude=models.CharField(max_length=256)
    city=models.CharField(max_length=256,null=True)
    image=models.ImageField(upload_to='image',blank=True,null=True)
    class Meta:
        verbose_name_plural='hospitals'
        ordering=['name']
    def __str__(self):
        return self.name
