from django.db import models


# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=80)
    score = models.IntegerField(default=0)
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, null=True)


class Card(models.Model):
    img_url = models.TextField()
    artist = models.TextField()
    player = models.ForeignKey('Player', on_delete=models.CASCADE)


class Session(models.Model):
    code = models.CharField(max_length=16)
