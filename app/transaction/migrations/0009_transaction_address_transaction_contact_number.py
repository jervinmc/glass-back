# Generated by Django 4.0.1 on 2023-01-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_transaction_tracking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='contact_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='contact_number'),
        ),
    ]