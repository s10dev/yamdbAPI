# Generated by Django 3.0.5 on 2021-04-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_auto_20210403_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]