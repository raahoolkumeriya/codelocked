# Generated by Django 2.1 on 2018-11-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_streamtype_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamtype',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]
