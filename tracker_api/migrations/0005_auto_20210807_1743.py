# Generated by Django 2.2 on 2021-08-07 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_api', '0004_auto_20210807_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
