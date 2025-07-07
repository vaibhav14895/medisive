from django.db import models

# Create your models here.
class Costumer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    message = models.TextField()
    def __str__(self):
        return self.name