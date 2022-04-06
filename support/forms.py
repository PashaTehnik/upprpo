from django import forms

class SupportForm(forms.Form):
    game = forms.CharField()
    problem = forms.CharField()
    description = forms.CharField()