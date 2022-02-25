from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import RegistrForm
from django.contrib.auth.models import User

# Функция регистрации
def register(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return registration_complete(request)
        if form.data['password1'] != form.data['password2']:
            return diff_passwords(request)
        if User.objects.filter(username=form.data['username']).exists():
            return name_exist(request)
        return HttpResponse("Ooooops.. Попробуй еще раз, возможно это имя пользователя занято.")
    else:  # Иначе
        # Создаём форму
        form = RegistrForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, "registration/register.html", data)


def index(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def registration_complete(request):
    template = loader.get_template('registration/registration_complete.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def diff_passwords(request):
    template = loader.get_template('registration/diff_passwords.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def name_exist(request):
    template = loader.get_template('registration/name_exist.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


