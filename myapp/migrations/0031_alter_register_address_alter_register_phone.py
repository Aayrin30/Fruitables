# Generated by Django 5.0.6 on 2024-07-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_alter_register_address_alter_register_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
