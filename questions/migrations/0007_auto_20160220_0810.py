# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_question_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='author_id',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(default=b''),
        ),
    ]
