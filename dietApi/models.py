from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=200)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()