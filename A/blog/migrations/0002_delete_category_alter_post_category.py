# Generated by Django 4.0 on 2021-12-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='shop.Category'),
        ),
    ]