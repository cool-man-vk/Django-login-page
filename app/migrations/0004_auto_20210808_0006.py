# Generated by Django 3.2.6 on 2021-08-07 18:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210808_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2021, 8, 7, 18, 36, 20, 624858, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='details',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2021, 8, 7, 18, 36, 20, 624858, tzinfo=utc)),
        ),
    ]