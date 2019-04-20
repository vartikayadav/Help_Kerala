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
class Patient(models.Model):
    name=models.CharField(max_length=256)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True,blank=True)
    problem=models.CharField(max_length=256,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='Patients'
        ordering=['date_added']
    def __str__(self):
        return self.name
