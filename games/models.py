from django.conf import settings
from django.db import models
import datetime
from django.utils import timezone
from django import forms
from PIL import Image
from os import path


class GameHtml5(models.Model):
    src = models.CharField(max_length=500)
    CHOICES = [
            ('arcade', 'arcade'),
    ]
    genre = models.CharField(max_length=300, choices=CHOICES)
    description = models.CharField(max_length=500)
    id = models.CharField(primary_key=True, max_length=100)
    image = models.ImageField(upload_to='images/', default='images/no-image.jpg')

    def icon_image_250(self):
        size = (int(250*16/9), 250)
        pth = self.image.url
        #pth = pth[:-4]
        pth, ext = path.splitext(pth)
        pth += '_' + size[0].__str__() + 'x' + size[1].__str__() + ext
        try:
            Image.open(str(settings.BASE_DIR) + pth)
        except FileNotFoundError:
            original_image = Image.open(str(settings.BASE_DIR) + self.image.url)
            resized_image = original_image.resize(size)
            resized_image.save(str(settings.BASE_DIR) + pth)
            print("file", pth, "created")
        return pth


