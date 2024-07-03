# Generated by Django 5.0.6 on 2024-07-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0020_alter_company_options_remove_company_display_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['importer_name'], 'verbose_name_plural': 'companies'},
        ),
        migrations.RemoveField(
            model_name='company',
            name='affiliations',
        ),
        migrations.AddField(
            model_name='company',
            name='affiliations',
            field=models.ManyToManyField(blank=True, null=True, to='jobsearch.group'),
        ),
    ]
