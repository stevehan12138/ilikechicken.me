# Generated by Django 3.1.7 on 2021-03-02 20:39

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='body',
            field=martor.models.MartorField(),
        ),
    ]
