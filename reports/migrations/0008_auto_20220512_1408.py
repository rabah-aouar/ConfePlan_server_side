# Generated by Django 3.1.7 on 2022-05-12 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20220512_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_of_submition',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 14, 8, 17, 724013), editable=False, max_length=100),
        ),
    ]