# Generated by Django 5.0.6 on 2024-07-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0015_alter_job_job_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importer_name', models.CharField(max_length=255)),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_size', models.CharField(blank=True, max_length=20, null=True)),
                ('co_link', models.CharField(blank=True, max_length=255, null=True)),
                ('affiliations', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='co_link',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_size',
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
