from django import forms


class SupportForm(forms.Form):
    game = forms.CharField(required=True)
    problem = forms.CharField(required=True)
    description = forms.CharField(required=True)