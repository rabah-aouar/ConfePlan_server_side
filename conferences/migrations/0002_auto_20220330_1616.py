# Generated by Django 3.1.7 on 2022-03-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='logo',
            field=models.ImageField(blank=True, default='hello', upload_to='logos'),
        ),
    ]
