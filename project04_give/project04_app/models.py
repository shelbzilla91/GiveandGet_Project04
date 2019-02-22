from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    photo_url = models.TextField()

class Centers(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

class List(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')
    Centers = models.ForeignKey(Centers, on_delete=models.CASCADE, related_name='lists')



