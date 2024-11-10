from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    img = models.ImageField(upload_to='profiles/')
