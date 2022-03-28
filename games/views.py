from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from upprpo import settings
from .models import GameHtml5
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.http import Http404


def game(request, game_id):
    message = {'ans': '', 'type': 'danger'}
    message['page'] = {'home': 'white', 'about': 'white', 'games': 'secondary', 'hz': 'white'}
    message['game'] = get_object_or_404(GameHtml5, pk=game_id)
    if not request.user.is_authenticated:
        message['ans'], message['type'] = "please log in to access this page", 'warning'
        message['game'] = ''
    return render(request, 'games/index.html', message)


class Games(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        """Return published games."""
        return GameHtml5.objects.order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Games, self).get_context_data(**kwargs)
        message = {'ans': '', 'type': 'danger'}
        message['page'] = {'home': 'white', 'about': 'white', 'games': 'secondary', 'hz': 'white'}
        return {**message, **context}
