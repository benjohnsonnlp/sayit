import logging
import os

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from sayit.models import Player

logger = logging.getLogger("views")


def index(request):
    return render(request, "sayit/index.html", context=None)


def secret():
    return os.environ['unsplash_access']


def get_hand(quantity):
    key = secret()
    image_urls = []
    url = "https://api.unsplash.com/photos/random?client_id={}&count={}&query=surreal".format(key.strip(), quantity)
    print("Getting images from {}".format(url))
    response = requests.get(url).json()
    image_urls.append(response['urls']['raw'])

    return image_urls


def play(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    players = Player.objects.filter()
    hand_of_cards = get_hand(6)
    context = {
        "hand": hand_of_cards,
        "player": player,
        "players": players,
    }
    return render(request, "sayit/play.html", context=context)


def save_player(request):
    players_name = request.POST["name"]
    player = Player(name=players_name)
    player.save()
    return HttpResponseRedirect(reverse("play", args=[player.id]))
