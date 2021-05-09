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




def play(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    players = Player.objects.filter()
    player.deal_hand()
    context = {
        "hand": [img.img_url for img in player.card_set.all()],
        "player": player,
        "players": players,
    }
    return render(request, "sayit/play.html", context=context)


def save_player(request):
    players_name = request.POST["name"]
    player = Player(name=players_name)
    player.save()
    return HttpResponseRedirect(reverse("play", args=[player.id]))
