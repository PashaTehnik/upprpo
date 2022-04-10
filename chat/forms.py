from django import forms


class MessageForm(forms.Form):
    text = forms.CharField(max_length=1000, )
    image = forms.ImageField()


class MultiForm(forms.Form):
    file = forms.FileField()
    # image = forms.ImageField(upload_to='chat_images/', blank=True)
    # file = forms.FileField(upload_to='chat_files/', blank=True)
