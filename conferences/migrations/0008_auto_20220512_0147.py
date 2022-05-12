# Generated by Django 3.1.7 on 2022-05-12 00:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0007_auto_20220427_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='conference',
            name='start_submition_date',
            field=models.DateTimeField(default=datetime.datetime.now, max_length=100),
        ),
        migrations.CreateModel(
            name='ConferneceStatusHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=100)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='conferences.conference')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='conferences.conferencestatus')),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceDatesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=100)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='conferences.conference')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='conferences.datetype')),
            ],
        ),
    ]
