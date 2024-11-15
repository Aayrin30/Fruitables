# Generated by Django 5.0.6 on 2024-06-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('companyname', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('zip', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
    ]
