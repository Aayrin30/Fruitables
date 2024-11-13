# Generated by Django 5.0.6 on 2024-06-19 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]