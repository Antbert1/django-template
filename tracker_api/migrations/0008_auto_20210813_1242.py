# Generated by Django 2.2 on 2021-08-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_api', '0007_answer_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='period',
            field=models.BooleanField(),
        ),
    ]
