# Generated by Django 2.0.9 on 2018-12-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20181206_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=350),
        ),
    ]