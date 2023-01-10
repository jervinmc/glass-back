# Generated by Django 4.0.1 on 2022-12-28 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_from',
        ),
        migrations.AddField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created'),
        ),
    ]