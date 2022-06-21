from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers


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


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    author = serializers.CharField(source='author.username', max_length=300)
    pub_date = serializers.DateTimeField()


class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class ChatSerializer(serializers.ModelSerializer):

    messages = MessageSerializer(read_only=True, many=True)
    members = MembersSerializer(read_only=True, many=True)

    class Meta:
        model = Chat
        fields = ('messages', 'members')

