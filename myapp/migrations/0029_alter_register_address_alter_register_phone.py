# Generated by Django 5.0.6 on 2024-07-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_register_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(blank=True, default=1234567890, max_length=15, null=True),
        ),
    ]
