# Generated by Django 5.0.6 on 2024-07-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_total',
            field=models.IntegerField(null=True),
        ),
    ]
