# Generated by Django 2.1.5 on 2021-07-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210730_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(),
        ),
    ]