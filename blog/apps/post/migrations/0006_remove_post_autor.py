# Generated by Django 5.0 on 2023-12-19 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
    ]
