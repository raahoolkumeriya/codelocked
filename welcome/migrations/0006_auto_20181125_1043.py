# Generated by Django 2.1 on 2018-11-25 05:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0005_auto_20181124_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamtype',
            name='summary',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='streamtype',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
