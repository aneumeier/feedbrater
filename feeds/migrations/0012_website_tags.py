# Generated by Django 3.0.7 on 2020-10-23 09:42

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('feeds', '0011_add_kservice_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
