from django.test import TestCase
from main.models import About


class AboutTestCase(TestCase):

    def setUp(self):
        About.objects.create(string="Abouttest hmmmm", size=15)

    def test_object_created(self):
        about = About.objects.all().last().__dict__

        self.assertEqual(about['string'], "Abouttest hmmmm")
