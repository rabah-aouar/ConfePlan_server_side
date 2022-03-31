# Generated by Django 3.1.7 on 2022-03-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_auto_20220330_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='is_accepted',
        ),
        migrations.AddField(
            model_name='conference',
            name='status',
            field=models.CharField(default='waiting', max_length=15),
        ),
    ]