from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.contrib import auth
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def index(request):
    window = """<div class="okno">
      Всплывающее окошко!
    </div>"""
    return render(request, 'main/index.html', {'window': window})


def logout_(request):
    logout(request)
    return redirect('/')

# def game(request, game_id):
#     game = get_object_or_404(GameHtml5, pk=game_id)
#     return render(request, 'games/index.html', {'game': game})
