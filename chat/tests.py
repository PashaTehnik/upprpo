from django.test import TestCase
from chat.models import MessageSerializer, Chat, Message
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


class MessageTest(TestCase):
    def setUP(self):
        time = timezone.now()
        User.objects.create("adm")
        user = authenticate("adm")
        Message.objects.create(text="Testing", author=user, pub_date=time)

    def test_message_created(self):
        #author = Message.objects.all().last().author
        #text = Message.objects.all().last().text
        print(User.objects.all())
        self.assertIsNotNone(Message.objects.all().last())
        #self.assertEqual(text, 'Testing')
        #self.assertEqual(author.username, 'admin')

# Create your tests here.
