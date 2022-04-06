from django.shortcuts import render, get_object_or_404
from .forms import SupportForm
from games.models import GameHtml5
from django.core.mail import mail_admins, send_mail
from django.conf import settings
from django.shortcuts import redirect, reverse


# Create your views here.
def index(request):

    message = {'games': GameHtml5.objects.order_by('-id'), 'messageSent': False}
    message['page'] = {'home': 'white', 'support': 'secondary', 'chat': 'white', 'about': 'white', 'games': 'white',
                       'hz': 'white'}
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():

            cd = form.cleaned_data
            game = cd['game']
            problem = cd['problem']
            description = cd['description']
            print(game, description, problem)
            theme = game + ':' + problem
            #send_mail(theme, description, settings.DEFAULT_FROM_EMAIL, settings.DEFAULT_TO_EMAIL)
            mail_admins(theme, description)
            message = {'ans': "Thank you for contacting us, your issue will be handled. (no)", 'type': 'success'}

    else:
        form = SupportForm()

    return render(request, 'support/index.html', message)
