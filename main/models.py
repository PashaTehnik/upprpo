from django.db import models


class About(models.Model):
    size = models.IntegerField(help_text="Enter font size(1 - big, 10 - small)", default=10)
    string = models.CharField(max_length=255, blank=True)
