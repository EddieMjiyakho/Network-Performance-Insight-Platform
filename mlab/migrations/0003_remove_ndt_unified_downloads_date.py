# Generated by Django 5.0.7 on 2024-09-11 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlab', '0002_ndt_unified_downloads_ndt_unified_uploads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ndt_unified_downloads',
            name='date',
        ),
    ]
