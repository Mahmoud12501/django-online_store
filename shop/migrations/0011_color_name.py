# Generated by Django 4.0.4 on 2022-06-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_color_clothe_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
