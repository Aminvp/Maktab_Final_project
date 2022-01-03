# Generated by Django 4.0 on 2022-01-01 20:33

from django.db import migrations, models


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
                ('full_name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
