# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-27 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('journals', '0002_auto_20180322_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
        ),
        migrations.AddField(
            model_name='journal',
            name='video_course_ids',
            field=jsonfield.fields.JSONField(default={'course_runs': []}, help_text='List of course IDs to pull videos from', verbose_name='Video Source Course IDs'),
        ),
        migrations.AddField(
            model_name='video',
            name='source_course_run',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='journal',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journals.Organization'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='display_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='transcript_url',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='view_url',
            field=models.URLField(max_length=255),
        ),
    ]
