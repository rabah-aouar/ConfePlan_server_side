# Generated by Django 3.1.7 on 2022-03-30 14:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('family_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('full_adress', models.CharField(max_length=255)),
                ('linked_in_username', models.CharField(max_length=255)),
                ('fields_of_interssts', models.CharField(max_length=255)),
                ('bio', models.CharField(default='this is bio', max_length=1000)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
