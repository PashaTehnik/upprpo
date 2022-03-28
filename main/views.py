from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.contrib import auth
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from .models import About


def user_login(request):
    # print(request.GET)
    # print(request.POST)
    message = {'ans': '', 'type': 'danger'}
    message['page'] = {'home': 'secondary', 'about': 'white', 'games': 'white', 'hz': 'white'}

    if request.method == 'POST':
        if request.POST['next'] == 'login':
            print(request.POST)
            form = RegisterForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        message['ans'] = 'successfully logged in'
                        message['type'] = 'success'
                        #return redirect('/')
                    else:
                        message['ans'] = 'Disabled account'
                else:
                    message['ans'] = 'Invalid login or password'

        elif request.POST['next'] == 'logout':
            logout_(request)
            return redirect('/')
        elif request.POST['next'] == 'registr':
            # form = RegisterForm(request.POST)
            # if form.is_valid():
            #     new_user = form.save(commit=False)
            #     new_user.set_password(form.cleaned_data['password'])
            #     new_user.save()
            return redirect('/')
    else:
        raise Exception('I dont know django! :`(')
        # form = RegisterForm()
    print(request, message)
    return render(request, 'main/index.html', message)


def index(request):
    message = {'ans': '', 'type': 'danger'}
    message['page'] = {'home': 'secondary', 'about': 'white', 'games': 'white', 'hz': 'white'}
    print(request.GET)
    print(request.POST)
    return render(request, 'main/index.html', message)


def about(request):
    message = {'ans': '', 'type': 'danger'}
    message['page'] = {'home': 'white', 'about': 'secondary', 'games': 'white', 'hz': 'white'}
    message['abouts'] = get_list_or_404(About)
    return render(request, 'main/index.html', message)


def logout_(request):
    logout(request)
    return redirect('/')

# def game(request, game_id):
#     game = get_object_or_404(GameHtml5, pk=game_id)
#     return render(request, 'games/index.html', {'game': game})
