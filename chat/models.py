from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django_extensions.db.models import TimeStampedModel
# from taggit.managers import TaggableManager


class Message(models.Model):
    text = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='chat_images/', blank=True)
    file = models.FileField(upload_to='chat_files/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)


class Chat(models.Model):
    CHOICES = [
        ('dialog', 'dialog'),
        ('chat', 'chat'),
    ]
    type = models.CharField(max_length=300, choices=CHOICES, default='dialog')
    members = models.ManyToManyField(User)
    message_set = models.ManyToManyField(Message)


class Photo(models.Model):
    file = models.ImageField(upload_to='chat_images/', blank=True)


class Photo(models.Model):
    file = models.ImageField(upload_to='media', default='media/images/no-image.jpg')
    #is_public = models.BooleanField(default=True)
    #tags = TaggableManager(blank=True, help_text=None)


