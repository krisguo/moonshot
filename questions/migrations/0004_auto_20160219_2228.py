# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='author_id',
        ),
    ]
