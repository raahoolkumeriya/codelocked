# Generated by Django 2.1.5 on 2019-07-16 04:11

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StreamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.CharField(max_length=30)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('github', models.URLField(blank=True)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tags', models.CharField(choices=[('PY', 'Python'), ('SH', 'Shell'), ('AN', 'ansible'), ('DJ', 'django'), ('ML', 'machine_learning'), ('HT', 'HTML'), ('CS', 'CSS')], max_length=2)),
            ],
            options={
                'verbose_name': 'Stream Entry',
                'verbose_name_plural': 'Stream Entries',
                'ordering': ['-created'],
            },
        ),
    ]
