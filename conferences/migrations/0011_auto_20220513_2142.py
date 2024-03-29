# Generated by Django 3.1.7 on 2022-05-13 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0010_remove_confernecestatushistory_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencedateshistory',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.conference'),
        ),
        migrations.AlterField(
            model_name='conferencedateshistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.datetype'),
        ),
        migrations.AlterField(
            model_name='confernecestatushistory',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.conference'),
        ),
        migrations.AlterField(
            model_name='confernecestatushistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.conferencestatus'),
        ),
    ]
