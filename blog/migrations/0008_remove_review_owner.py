# Generated by Django 4.0.4 on 2022-06-12 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='owner',
        ),
    ]
