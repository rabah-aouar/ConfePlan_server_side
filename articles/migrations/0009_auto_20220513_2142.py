# Generated by Django 3.1.7 on 2022-05-13 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20220512_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articledateshistory',
            name='Article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlestatushistory',
            name='Article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlestatushistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articlestatus'),
        ),
    ]