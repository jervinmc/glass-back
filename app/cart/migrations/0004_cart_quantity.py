# Generated by Django 4.0.1 on 2022-12-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cart_product_id_cart_price_cart_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0.0, verbose_name='quantity'),
        ),
    ]
