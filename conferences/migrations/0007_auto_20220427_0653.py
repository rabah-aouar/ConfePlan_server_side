# Generated by Django 3.1.7 on 2022-04-27 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0006_auto_20220403_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='accepted_articles',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='pending_articles',
        ),
        migrations.AddField(
            model_name='conference',
            name='submition_deadline',
            field=models.DateTimeField(default=datetime.datetime.now, max_length=100),
        ),
    ]