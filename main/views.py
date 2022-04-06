from django.conf import settings
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
from django.core.mail import send_mail
from random import choice
from string import digits


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
            elif User.objects.filter(username=username) and User.objects.filter(username=username)[0].is_active:
                message['ans'] = 'user already exist'
                message['type'] = 'danger'
                print("user already exist")

            else:
                user = User(username=username, email=email)
                if user is not None:
                    if User.objects.filter(username=username):
                        tmp = User.objects.filter(username=username)[0]
                        tmp.delete()
                    user.set_password(passwd1)
                    user.is_active = False
                    user.save()
                    message['ans'] = 'please check your email box'
                    message['type'] = 'success'
                    theme = 'email confirmation'
                    code = ''.join(choice(digits) for _ in range(6))
                    message['conf_code'] = hash(code)
                    message['user'] = user.username
                    mess = 'please enter this code ' + code + ' to confirm this email.'
                    send_mail(theme, mess, settings.DEFAULT_FROM_EMAIL, [user.email])
                    print(mess, '\nto', [user.email], '\n', "all is ok")
        elif request.POST['next'] == 'conf':
            #print(type(request.POST['code']))
            # print(request.POST['code'])
            # print(hash(request.POST['code']))
            # print(int(request.POST['conf_code']))
            if hash(request.POST['code']) == int(request.POST['conf_code']):
                print("zbs")
                user = User.objects.filter(username=request.POST['user'])[0]
                user.is_active = True
                user.save()
                message['ans'] = 'success'
                message['type'] = 'success'
            else:
                message['ans'] = 'incorrect code, try again'
                message['type'] = 'danger'
                message['conf_code'] = request.POST['conf_code']
                message['user'] = request.POST['user']

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
