# Generated by Django 5.0.6 on 2024-07-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_remove_register_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
