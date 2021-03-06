from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    dateOfBirth = models.DateField(null=True)
    height = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    questionText = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionOption = models.ForeignKey(QuestionOption, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    MAC = models.CharField(max_length=200)
    WC = models.CharField(max_length=200)
    HC = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

# class Activity(models.Model):
#     name = models.CharField(max_length=200)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     updatedAt = models.DateTimeField(auto_now_add=True)

class PhysicalActivity(models.Model):
    # activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activityType = models.CharField(max_length=200, default="hobbies")
    activityName = models.CharField(max_length=400)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)