from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.contrib import auth
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm


def user_login(request):
    # print(request.GET)
    # print(request.POST)
    message = {'ans': ''}
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
                        return redirect('/')
                    else:
                        #return HttpResponse('Disabled account')
                        message['ans'] = 'Disabled account'
                else:
                    message['ans'] = 'Invalid login or password'
                    # return HttpResponse('Invalid login')

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
    print(request.GET)
    print(request.POST)
    return render(request, 'main/index.html')


def logout_(request):
    logout(request)
    return redirect('/')

# def game(request, game_id):
#     game = get_object_or_404(GameHtml5, pk=game_id)
#     return render(request, 'games/index.html', {'game': game})
