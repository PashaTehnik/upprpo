from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    mail = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
