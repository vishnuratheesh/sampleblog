# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name='articles', blank=True, to='articles.Category', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='extra_image',
            field=models.FileField(max_length=500, null=True, upload_to=b'images', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='hero_image',
            field=models.FileField(max_length=500, upload_to=b'images'),
        ),
    ]
