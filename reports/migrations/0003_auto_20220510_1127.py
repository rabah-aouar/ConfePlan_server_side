# Generated by Django 3.1.7 on 2022-05-10 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20220509_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_of_submition',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 11, 27, 53, 282478), editable=False, max_length=100),
        ),
    ]
