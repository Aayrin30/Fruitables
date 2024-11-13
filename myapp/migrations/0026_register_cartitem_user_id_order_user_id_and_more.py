# Generated by Django 5.0.6 on 2024-07-13 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_remove_rating_user_id_remove_order_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('otp', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.IntegerField(blank=True, default=1234567890, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register'),
        ),
    ]
