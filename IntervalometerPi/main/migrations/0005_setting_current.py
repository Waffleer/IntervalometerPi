# Generated by Django 4.2.5 on 2024-02-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_setting_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
