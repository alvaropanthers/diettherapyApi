from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    height = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

class Question:
    question = models.CharField(max_length=200)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()