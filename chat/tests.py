from django.test import TestCase, Client
from chat.models import Message, MessageSerializer
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from chat import views
import json
class MessageTestCase(TestCase):

    def setUp(self):
        #User.objects.create_user(username="admino")
        u, created = User.objects.get_or_create(username="admino")
        user = User.objects.all().last()
        Message.objects.create(text="Testing", author=user)

    def test_message_created(self):
        author = Message.objects.all().last().author
        text = Message.objects.all().last().text
        u, created = User.objects.get_or_create(username="admino")
        #print(User.objects.all())
        self.assertIsNotNone(User.objects.all().last())
        self.assertEqual(text, 'Testing')
        self.assertEqual(author.username, 'admino')


class MessageApiTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user("odin")
        User.objects.create_user("vtoroy")
        user_1 = User.objects.all().last()
        user_2 = User.objects.all().first()
        Message.objects.create(text="Testing", author=user_1)
        Message.objects.create(text="Testing1", author=user_2)
        Message.objects.create(text="Testing2", author=user_2)
        Message.objects.create(text="Testing3", author=user_1)
        Message.objects.create(text="Testing4", author=user_2)

    def test_api(self):
        url = reverse('chat:message_api')

        response_on_python = self.client.get(url, format='json').content
        #or item in response_on_python:
        response_on_python = response_on_python.decode("utf-8")
        response_on_python = json.loads(response_on_python)
        print(response_on_python[0])
        self.assertEqual(response_on_python[0]['author'],
                         'vtoroy'
                         )
        self.assertEqual(response_on_python[1]['author'],
                         'odin'
                         )
        self.assertEqual(response_on_python[3]['author'],
                         'vtoroy'
                         )
        self.assertEqual(response_on_python[0]['text'],
                         'Testing'
                         )
        self.assertEqual(response_on_python[2]['text'],
                         'Testing2'
                         )
        self.assertEqual(response_on_python[4]['text'],
                         'Testing4'
                         )





