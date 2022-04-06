from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.contrib import auth
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from .models import About
from django.contrib.auth.models import User


def user_login(request):
    # print(request.GET)
    # print(request.POST)
    message = {'ans': '', 'type': 'danger'}
    message['page'] = {'home': 'secondary', 'support': 'white', 'chat': 'white', 'about': 'white', 'games': 'white', 'hz': 'white'}

    if request.method == 'POST':
        print(request.POST)
        if request.POST['next'] == 'login':
            print(request.POST)
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        message['ans'] = 'successfully logged in'
                        message['type'] = 'success'
                        # return redirect('/')
                    else:
                        message['ans'] = 'Disabled account'
                else:
                    message['ans'] = 'Invalid login or password'

        elif request.POST['next'] == 'logout':
            logout_(request)
            return redirect('/')
        elif request.POST['next'] == 'registr':
            print(request.POST)
            print("registr")
            username, email, passwd1, passwd2 = request.POST.get('username'), request.POST.get('email'), \
                                                request.POST.get('password1'), request.POST.get('password2')
            if passwd1 != passwd2:
                message['ans'] = 'bad passwords'
                message['type'] = 'danger'
                print("bad passwd")
            elif User.objects.filter(username=username):
                message['ans'] = 'user already exist'
                message['type'] = 'danger'
                print("user already exist")

            else:
                user = User(username=username, email=email)
                if user is not None:
                    user.set_password(passwd1)
                    user.save()
                    user.is_active = True
                    message['ans'] = 'successfully'
                    message['type'] = 'success'
                    print("all is ok")

    else:
        raise Exception('I dont know django! :`(')
        # form = RegisterForm()
    print(request, message)
    return render(request, 'main/index.html', message)


def index(request):
    message = {'ans': '', 'type': 'danger'}
    message['page'] = {'home': 'secondary', 'support': 'white', 'chat': 'white', 'about': 'white', 'games': 'white', 'hz': 'white'}
    print(request.GET)
    print(request.POST)
    return render(request, 'main/index.html', message)


def about(request):
    message = {'ans': '', 'type': 'danger'}
    message['page'] = {'home': 'white', 'support': 'white', 'chat': 'white', 'about': 'secondary', 'games': 'white', 'hz': 'white'}
    message['abouts'] = get_list_or_404(About)
    return render(request, 'main/index.html', message)


def logout_(request):
    logout(request)
    return redirect('/')
