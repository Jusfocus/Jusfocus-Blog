# Generated by Django 2.0.9 on 2018-12-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=350),
        ),
    ]
