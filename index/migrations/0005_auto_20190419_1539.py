# Generated by Django 2.2 on 2019-04-19 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190418_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleimage',
            old_name='ImageTitle',
            new_name='image_title',
        ),
        migrations.RenameField(
            model_name='articleimage',
            old_name='ImageURL',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='pttarticle',
            old_name='ArticleDate',
            new_name='article_date',
        ),
        migrations.RenameField(
            model_name='pttarticle',
            old_name='ArticleTitle',
            new_name='article_title',
        ),
    ]
