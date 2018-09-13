# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 17:05
from __future__ import unicode_literals

from django.db import migrations
import journals.apps.journals.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0025_auto_20180902_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', journals.apps.journals.blocks.JournalRichTextBlock(features=['h1', 'h2', 'h3', 'ol', 'ul', 'bold', 'italic', 'link', 'hr', 'document-link', 'image'])), ('raw_html', journals.apps.journals.blocks.JournalRawHTMLBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Override image title', required=False)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'ol', 'ul', 'bold', 'italic', 'link', 'hr', 'document-link'], help_text='Override image caption', required=False))))), ('pdf', wagtail.wagtailcore.blocks.StructBlock((('doc', wagtail.wagtaildocs.blocks.DocumentChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Override document title', required=False))))), ('xblock_video', wagtail.wagtailcore.blocks.StructBlock((('video', journals.apps.journals.blocks.VideoChooserBlock(required=True)), ('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Override video title', required=False)))))), blank=True),
        ),
    ]