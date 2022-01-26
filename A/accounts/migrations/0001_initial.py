# Generated by Django 4.0 on 2022-01-25 12:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('full_name', models.CharField(max_length=120)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('channel', models.CharField(choices=[('Android', 'Android'), ('ios', 'Ios'), ('Web', 'Web')], max_length=12, verbose_name='channel')),
                ('phone', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=4, null=True)),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField(default=datetime.datetime(2022, 1, 25, 12, 26, 41, 7797, tzinfo=utc))),
                ('receipt_id', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'One Time Password',
                'verbose_name_plural': 'One Time Passwords',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
