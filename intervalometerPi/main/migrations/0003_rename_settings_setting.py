# Generated by Django 4.2.5 on 2024-02-29 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_settings_intervalseconds_settings_plenseconds'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings',
            new_name='Setting',
        ),
    ]