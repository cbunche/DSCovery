# Generated by Django 5.0.6 on 2024-05-15 18:42

import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2),
        ),
    ]
