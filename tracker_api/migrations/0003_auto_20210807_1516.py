# Generated by Django 2.2 on 2021-08-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_api', '0002_auto_20210807_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
