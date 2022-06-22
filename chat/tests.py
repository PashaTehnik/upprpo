from django.test import TestCase
from chat.models import Message
from django.contrib.auth.models import User


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
        print(User.objects.all())
        self.assertIsNotNone(User.objects.all().last())
        self.assertEqual(text, 'Testing')
        self.assertEqual(author.username, 'admino')


