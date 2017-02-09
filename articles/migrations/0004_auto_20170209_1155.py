# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify


def generate_slug(apps, schema_editor):
    Article = apps.get_model("articles", "Article")
    for article in Article.objects.all():
        if not article.slug:
            article.slug = slugify(article.title)
            article.save()

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_slug'),
    ]

    operations = [
         migrations.RunPython(generate_slug),
    ]
    
