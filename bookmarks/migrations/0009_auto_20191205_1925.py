# Generated by Django 2.2.7 on 2019-12-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0008_auto_20191205_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='alt',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='lat',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='lon',
            field=models.TextField(default='', max_length=100),
        ),
    ]
