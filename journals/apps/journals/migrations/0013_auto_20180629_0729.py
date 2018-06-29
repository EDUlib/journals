# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-29 07:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0040_page_draft_title'),
        ('journals', '0012_auto_20180523_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPageVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_at', models.DateTimeField(auto_now=True)),
                ('stale', models.BooleanField(default=False, help_text='Marked the object stale if the published date of visited page is later than visited at.')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
