# Generated by Django 5.0.6 on 2024-06-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0012_remove_jobsearch_level_remove_jobsearch_recency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
