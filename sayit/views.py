from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from sayit.models import Player


def index(request):
    return render(request, "sayit/index.html", context=None)


def play(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    players = Player.objects.filter()

    context = {
        "player": player,
        "players": players,
    }
    return render(request, "sayit/play.html", context=context)


def save_player(request):
    players_name = request.POST["name"]
    player = Player(name=players_name)
    player.save()
    return HttpResponseRedirect(reverse("play", args=[player.id]))