import os

import requests
from django.db import models


def secret():
    return os.environ['unsplash_access']

HAND_SIZE = 6

class Player(models.Model):
    name = models.CharField(max_length=80)
    score = models.IntegerField(default=0)
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, null=True)

    def deal_hand(self):
        key = secret()
        image_urls = []
        hand = list(self.card_set.all())
        quantity = HAND_SIZE - len(hand)
        if quantity > 0:
            url = "https://api.unsplash.com/photos/random?client_id={}&count={}&query=surreal".format(key.strip(), quantity)
            print("Getting images from {}".format(url))
            for image in requests.get(url).json():
                card = Card(player=self, img_url=image['urls']['raw'], artist="n/a")
                card.save()



class Card(models.Model):
    img_url = models.TextField()
    artist = models.TextField()
    player = models.ForeignKey('Player', on_delete=models.CASCADE)


class Session(models.Model):
    code = models.CharField(max_length=16)
