# Generated by Django 3.1.7 on 2021-03-02 23:04

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20210302_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='body',
            field=martor.models.MartorField(),
        ),
    ]
