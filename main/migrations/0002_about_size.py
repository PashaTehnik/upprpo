# Generated by Django 4.0.3 on 2022-03-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='size',
            field=models.IntegerField(default=10, help_text='Enter font size(1 - big, 10 - small)'),
        ),
    ]