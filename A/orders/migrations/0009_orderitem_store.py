# Generated by Django 4.0 on 2022-01-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_orderitem_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='store',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]