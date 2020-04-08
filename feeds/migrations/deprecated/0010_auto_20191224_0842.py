# Generated by Django 2.2.4 on 2019-12-24 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_sqash_migrations_09_14'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Short descriptive name for this category.', max_length=200, unique=True)),
                ('slug', models.SlugField(help_text='Short descriptive unique name for use in urls.', max_length=255, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='feeds.EditorCategory')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
                'unique_together': {('name', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='website',
            name='category',
            field=models.ManyToManyField(related_name='website_category', to='feeds.EditorCategory'),
        ),
    ]