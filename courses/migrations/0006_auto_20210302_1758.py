# Generated by Django 3.1.7 on 2021-03-02 22:58

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='body',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
