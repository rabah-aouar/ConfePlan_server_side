# Generated by Django 3.1.7 on 2022-05-12 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0009_auto_20220512_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confernecestatushistory',
            name='date',
        ),
    ]
