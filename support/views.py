from django.shortcuts import render, get_object_or_404
from .forms import SupportForm
from games.models import GameHtml5
from django.core.mail import mail_admins, send_mail
from django.conf import settings
from django.shortcuts import redirect, reverse


# Create your views here.
def index(request):

    message = {'games': GameHtml5.objects.order_by('-id'), 'messageSent': False}
    if request.method == 'POST':
        print(request.POST)
        form = SupportForm(request.POST)
        print(form)
        # check if data from the form is clean
        print(form.is_valid())
        if form.is_valid():

            cd = form.cleaned_data
            #subject = "Sending an email with Django"
            game = cd['game']
            problem = cd['problem']
            description = cd['description']
            print(type(game), description, problem)
            theme = game + ':' + problem

            # send the email to the recipent
            send_mail(theme, description, settings.DEFAULT_FROM_EMAIL, ['v.babushkin@g.nsu.ru'],)

            # set the variable initially created to True
            message['messageSent'] = True



    else:
        form = SupportForm()

    return render(request, 'support/index.html', message)
