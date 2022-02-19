from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import RegistrForm


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


