# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-18 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('journals', '0015_auto_20180717_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalpage',
            name='images',
            field=models.ManyToManyField(to='wagtailimages.Image'),
        ),
    ]
