# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-14 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='authordetails',
            name='website',
            field=models.URLField(default='', max_length=60, verbose_name='个人主页'),
        ),
    ]
