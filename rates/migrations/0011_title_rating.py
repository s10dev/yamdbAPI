# Generated by Django 3.0.5 on 2021-04-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0010_auto_20210406_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='рейтинг'),
        ),
    ]
