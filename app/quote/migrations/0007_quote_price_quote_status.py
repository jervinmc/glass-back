# Generated by Django 4.0.1 on 2023-01-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0006_quote_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='quote',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='status'),
        ),
    ]