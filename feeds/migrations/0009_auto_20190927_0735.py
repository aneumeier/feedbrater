# Generated by Django 2.2.4 on 2019-09-27 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0008_post_guidislink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='summary',
        ),
    ]