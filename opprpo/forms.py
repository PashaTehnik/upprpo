from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email
    email = forms.EmailField(max_length=254, help_text='Нужен для восстановления пароля')

    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'password1', 'password2',)
