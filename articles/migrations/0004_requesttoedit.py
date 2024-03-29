# Generated by Django 3.1.7 on 2022-04-27 05:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_article_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestToEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification', models.TextField(max_length=10000)),
                ('deadline', models.DateTimeField()),
                ('date_of_creation', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
